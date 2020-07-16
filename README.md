# Password Generator

## Information
This is a python based command line tool used to generate a password using random characters or a supplied dictionary file.

## Example commands

### Help
Will list out all available commands and sample usage.

#### Base usage
`password.py --help`

`password.py -h`

### Random password
Will generate a password using random letters, numbers and symbols of the supplied length. Will default to 20 characters if no length is supplied. 

#### Base usage
`password.py --random`

`password.py -r`

#### With supplied length
`password.py --random --count 30`

`password.py -r -c 30`

### Dictionary based password
Will generate a password using random words from a supplied dictionary of the supplied length. Will default to internal dictionary if none is suppled. Will default to 3 words if none is supplied. Options for adding leading symbol to the password and seperator between words within the password. 

#### Base usage
`password.py --dictionary`

`password.py -d`

#### With supplied length
`password.py --dictionary --count 4`

`password.py -d -c 4`

#### With supplied dictionary
`password.py --dictionary --file /path`

`password.py -d -f /path`

#### With leading symbol
`password.py --dictionary --leadingSymbol`

`password.py -d -l`

#### With seperator
`password.py --dictionary --seperator`

`password.py -d -s`
