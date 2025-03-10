$files = @("index", "DL_CNN") # "DL_CNN", "DL_RNN", "DL_ANN"
$html_files = $files | ForEach-Object -Process {".\$_.html"}
$data_files = @("favicon-32x32.png")

$files | ForEach-Object -Process {python.exe .\render_abstract.py $_}
scp $html_files homel:~/public_html
scp $data_files homel:~/public_html