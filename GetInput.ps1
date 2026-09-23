$base_url = "https://adventofcode.com/"
$year = "2017"
$day = "1"
$session_id = $Env:SESSIONID
$cookie = [System.Net.Cookie]::new("session", $session_id)

# Hit the base url to create a session
$result = Invoke-WebRequest -UseBasicParsing -SessionVariable session -Uri $base_url -ErrorAction Stop

# Add session cookie to session
$session.Cookies.Add([uri]::new($base_url, "/"), $cookie)

# Get the input
$input_url = $base_url + "$year/day/$day/input"
$result = Invoke-WebRequest -UseBasicParsing -WebSession $session -Uri $input_url -ErrorAction Stop

# Input should be plain text file
if ($result.Headers["Content-Type"] -eq "text/plain") {
    $result.Content | Out-File -Encoding default -FilePath "day$day\input.txt"
}

