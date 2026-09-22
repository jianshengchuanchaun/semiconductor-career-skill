param([Parameter(Mandatory=$true)][string]$PresentationPath,[Parameter(Mandatory=$true)][string]$OutputDirectory)
$ErrorActionPreference = 'Stop'
$resolvedPresentation = (Resolve-Path -LiteralPath $PresentationPath).Path
$resolvedRoot = [IO.Path]::GetFullPath($OutputDirectory)
New-Item -ItemType Directory -Path $resolvedRoot -Force | Out-Null
$pptApp=$null
$openedPresentation=$null
try {
    $pptApp=New-Object -ComObject PowerPoint.Application
    if ($pptApp.Presentations.Count -ne 0) { throw 'PowerPoint has another open presentation. Stopping without modifying it.' }
    $openedPresentation=$pptApp.Presentations.Open($resolvedPresentation,$true,$false,$false)
    $openedPresentation.Export($resolvedRoot,'PNG',1600,900)
    $pdfPath=Join-Path $resolvedRoot 'presentation.pdf'
    $openedPresentation.SaveAs($pdfPath,32)
    $report=@{slide_count=$openedPresentation.Slides.Count;slide_width_pt=$openedPresentation.PageSetup.SlideWidth;slide_height_pt=$openedPresentation.PageSetup.SlideHeight;pdf=$pdfPath;source=$resolvedPresentation}
    $report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $resolvedRoot 'native-export.json') -Encoding utf8
    Write-Output ($report | ConvertTo-Json -Compress)
} finally {
    if ($null -ne $openedPresentation) { $openedPresentation.Close(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($openedPresentation) }
    if ($null -ne $pptApp) { if ($pptApp.Presentations.Count -eq 0) { $pptApp.Quit() }; [void][Runtime.InteropServices.Marshal]::ReleaseComObject($pptApp) }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
