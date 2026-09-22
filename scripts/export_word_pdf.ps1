param([Parameter(Mandatory=$true)][string]$DocumentPath, [Parameter(Mandatory=$true)][string]$PdfPath)
$ErrorActionPreference = 'Stop'
$resolvedDocument = (Resolve-Path -LiteralPath $DocumentPath).Path
$pdfParent = Split-Path -Parent $PdfPath
New-Item -ItemType Directory -Path $pdfParent -Force | Out-Null
$wordApp = $null
$openedDocument = $null
try {
    $wordApp = New-Object -ComObject Word.Application
    if ($wordApp.Documents.Count -ne 0) { throw 'New Word instance unexpectedly has open documents; stopping.' }
    $wordApp.Visible = $false
    $wordApp.DisplayAlerts = 0
    $openedDocument = $wordApp.Documents.Open($resolvedDocument, $false, $true)
    $openedDocument.Repaginate()
    $pageTotal = $openedDocument.ComputeStatistics(2)
    $openedDocument.ExportAsFixedFormat($PdfPath, 17)
    Write-Output ('Word export pages: ' + $pageTotal)
    Write-Output ('PDF: ' + $PdfPath)
}
finally {
    if ($null -ne $openedDocument) { $openedDocument.Close(0); [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($openedDocument) }
    if ($null -ne $wordApp) {
        if ($wordApp.Documents.Count -eq 0) { $wordApp.Quit(0) }
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($wordApp)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
