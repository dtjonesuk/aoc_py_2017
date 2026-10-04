function Get-PuzzleInput
{
    <#
.SYNOPSIS
    Retrieve an Advent of Code puzzle input


.NOTES
    Name: Get-PuzzleInput
    Author: David T. Jones
    Version: 1.0
    DateCreated: 2026-09-28


.EXAMPLE
    Get-Something -SessionId "<sessionid>" -Year 2026 -Month 1
#>

    [CmdletBinding()]
    param(
        [Parameter(
            Mandatory = $true,
            ValueFromPipeline = $true,
            ValueFromPipelineByPropertyName = $true,
            Position = 0
            )]
        [string]  $SessionId,

        [Parameter(
            Mandatory = $false
        )]
        [ValidateRange(2016, 2025)]
        [int] $Year,


        [Parameter(
            Mandatory = $false
        )]
        [ValidateRange(1,31)]
        [int] $Day
    )
    PROCESS {
        $base_url = "https://adventofcode.com/"
        $cookie = [System.Net.Cookie]::new("session", $SessionId)
        # Hit the base url to create a session
        $result = Invoke-WebRequest -UseBasicParsing -SessionVariable session -Uri $base_url -ErrorAction Stop

        # Add session cookie to session
        $session.Cookies.Add([uri]::new($base_url, "/"), $cookie)

        # Get the input
        $input_url = $base_url + "$Year/day/$Day/input"
        $result = Invoke-WebRequest -UseBasicParsing -WebSession $session -Uri $input_url -ErrorAction Stop

        # Input should be plain text file
        if ($result.Headers["Content-Type"] -eq "text/plain")
        {
            return $result.Content
        }
    }

}

$day = 13
$destination = "day$day"

# create directory
if (!(Test-Path -PathType Container $destination))
{
    New-Item -ItemType Directory -Path $destination
}

# copy template files
$exclude = Get-ChildItem -recurse $destination
Copy-Item "template\*.*" "day$day\" -Exclude $exclude

# get puzzle input
Get-PuzzleInput -SessionId $Env:SESSIONID -Year 2017 -Day $day | Out-File -Encoding default -FilePath "day$day\input.txt"
