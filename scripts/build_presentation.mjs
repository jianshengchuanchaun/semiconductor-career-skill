/** Editable PPTX builder. Set CODEX_NODE_MODULES, PRESENTATIONS_SKILL and RUNTIME_PYTHON. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const SKILL=process.env.PRESENTATIONS_SKILL;
const MOD=process.env.CODEX_NODE_MODULES;
if(!SKILL||!MOD||!process.env.RUNTIME_PYTHON) throw new Error('Set PRESENTATIONS_SKILL, CODEX_NODE_MODULES and RUNTIME_PYTHON');
process.env.RUNTIME_NODE_MODULES ??= MOD;
const {Presentation,PresentationFile}=await import(pathToFileURL(path.join(MOD,'@oai/artifact-tool/dist/artifact_tool.mjs')).href);
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const data=JSON.parse(await fs.readFile(path.join(ROOT,'presentations/talk-content.json'),'utf8'));
if(data.slides.length!==12||data.slides.reduce((a,s)=>a+s.seconds,0)!==600) throw new Error('Require 12 slides / 600 seconds');
const QA=path.join(ROOT,'.qa/presentation-v1.1');await fs.mkdir(QA,{recursive:true});
const p=Presentation.create({slideSize:{width:1280,height:720}});
const FONT='Microsoft YaHei',NAVY='#142C42',INK='#172C3D',MUTED='#4D6170',BLUE='#006D8B';
function text(s,value,x,y,w,h,size=26,color=INK,bold=false){
 const sh=s.shapes.add({geometry:'textbox',name:'text',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 sh.text=value;sh.text.style={typeface:FONT,fontSize:size,color,bold,autoFit:'none',verticalAlignment:'top',insets:{top:0,right:0,bottom:0,left:0}};return sh;
}
function base(s,d,i){s.background.fill='#FAFBFC';text(s,d.title,64,48,1152,70,44,NAVY,true);text(s,'我的模拟电路世界',64,674,650,26,17,MUTED);text(s,String(i+1).padStart(2,'0')+' / 12',1110,674,110,26,17,MUTED);}
function take(s,value,y=606){text(s,value,64,y,1152,54,24,BLUE,true);}
function table(s,values,widths,{top=159,height=405,font=25}={}){
 const t=s.tables.add({rows:values.length,columns:values[0].length,left:64,top,width:1152,height,columnWidths:widths,values});
 t.styleOptions={headerRow:true,bandedRows:false};
 t.borders.assign({style:'solid',fill:'#D3DEE6',width:1});
 const all=t.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length});
 all.assign({textStyle:{typeface:FONT,fontSize:font,color:INK,autoFit:'none'},margins:{left:16,right:14,top:15,bottom:12},anchor:'center'});
 for(let r=0;r<values.length;r++){
  t.rows[r].height=r===0?58:(height-58)/(values.length-1);
  for(let c=0;c<values[0].length;c++){
   const cell=t.getCell(r,c);cell.fill=r===0?NAVY:(r%2===0?'#EDF3F7':'#FFFFFF');
   cell.text.style={typeface:FONT,fontSize:font,color:r===0?'#FFFFFF':INK,bold:r===0,autoFit:'none',verticalAlignment:'middle',insets:{left:16,right:14,top:10,bottom:10}};
  }
 }
 return t;
}
const tableSlides=[];
for(const [i,d] of data.slides.entries()){
 const s=p.slides.add();
 if(d.kind==='cover'){
  s.background.fill='#071625';
  s.images.add({blob:new Uint8Array(await fs.readFile(path.join(ROOT,'assets/semiconductor-cover-v1.1.png'))),contentType:'image/png',alt:'AI生成的概念晶圆与无品牌芯片背景',fit:'cover',position:{left:0,top:0,width:1280,height:720}});
  text(s,d.title,72,132,745,176,68,'#FFFFFF',true);
  text(s,d.subtitle,76,358,770,84,30,'#D9F1F8');
  text(s,'我的模拟电路世界',76,555,680,46,28,'#FFFFFF',true);
  text(s,'就业导向 Skill  ·  10 分钟介绍',76,615,680,32,22,'#B5D3DF');
 }else{
  base(s,d,i);
  if(d.table){
   let widths=[370,782],opts={};
   if(['foreign','domestic'].includes(d.kind)){widths=[300,460,392];opts={height:403,font:24};}
   else if(d.kind==='jd'){widths=[323,432,397];opts={height:403,font:24};}
   else if(d.kind==='roadmap'){widths=[216,586,350];opts={height:403,font:25};}
   else if(d.kind==='budget'){widths=[814,338];opts={top:143,height:443,font:23};}
   table(s,d.table,widths,opts);tableSlides.push(i+1);take(s,d.takeaway,d.kind==='budget'?613:599);
  }else if(['dialog','review','install'].includes(d.kind)){
   text(s,d.left_title,64,171,537,58,34,BLUE,true);text(s,d.right_title,683,171,533,58,34,BLUE,true);
   text(s,d.left,64,258,541,273,29,INK);text(s,d.right,683,258,533,273,29,INK);
   take(s,d.takeaway,600);
  }else if(d.kind==='close'){
   text(s,d.prompt,64,191,1152,268,34,INK);
   text(s,d.takeaway,64,516,1152,97,27,BLUE,true);
  }
 }
 s.speakerNotes.textFrame.setText(`建议时长：${d.seconds} 秒\n\n${d.notes}\n\n来源与边界\n${d.sources.join('\n')}`);
}
const candidate=path.join(QA,'candidate.pptx');
const final=process.env.PRESENTATION_OUTPUT || path.join(ROOT,'presentations/半导体研一就业规划_10分钟推广_我的模拟电路世界_v1.1.0.pptx');
await fs.mkdir(path.dirname(final),{recursive:true});
await (await PresentationFile.exportPptx(p)).save(candidate);
console.log('CANDIDATE='+candidate);
await finalizePresentation({explicitTotalSlideCount:12,requiredNativeTableOwnerSlides:tableSlides,requiredNativeChartOwnerSlides:[],workspaceDir:ROOT,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.RUNTIME_PYTHON,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...tableSlides.flatMap(n=>['--require-native-table-slide',String(n)])],fontPolicy:{basis:'design',families:[FONT]},verifyArtifactToolImport:true,receiptPath:path.join(QA,`validation-${Date.now()}.json`)});
console.log('FINAL='+final);
for(const [i,slide] of p.slides.items.entries()){
 const blob=await p.export({slide,format:'png',scale:1});
 await fs.writeFile(path.join(QA,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
 const layout=await slide.export({format:'layout'});await fs.writeFile(path.join(QA,`slide-${String(i+1).padStart(2,'0')}.layout.json`),await layout.text());
 console.log('PREVIEW='+(i+1));
}
const script=['# 10 分钟推广讲稿','',`作者：${data.author}　版本：${data.version}`,'','共 12 页，建议总时长 600 秒。讲稿也已写入每页 PowerPoint 演讲者备注。排练时可按自己的语速调整。',''];
let elapsed=0;
for(const [i,d]of data.slides.entries()){const start=elapsed;elapsed+=d.seconds;const fmt=n=>`${Math.floor(n/60)}:${String(n%60).padStart(2,'0')}`;script.push(`## ${i+1}. ${d.title.replaceAll('\n','')}（${fmt(start)}–${fmt(elapsed)}）`,'',d.notes,'','来源与边界：',...d.sources.map(x=>'- '+x),'');}
await fs.writeFile(path.join(ROOT,'presentations/10分钟逐页讲稿.md'),script.join('\n'),'utf8');
console.log('DONE');
