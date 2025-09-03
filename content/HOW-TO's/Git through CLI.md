# Create Repo from CLI
## Usage:
#### Create a new GitHub repository.
 Use the "`ORG/NAME`" syntax to create a repository within your organization.
 ```
 gh repo create [<name>] [flags]
 ```
#### Flags:
 ```
 -d, --description string   Description of repository
     --enable-issues        Enable issues in the new repository (default true)
     --enable-wiki          Enable wiki in the new repository (default true)
 -h, --homepage string      Repository home page URL
     --public               Make the new repository public
 -t, --team string          The name of the organization team to be granted access
 ```
#### Global Flags:
 ```
  --help                  Show help for command
  -R, --repo OWNER/REPO   Select another repository using the OWNER/REPO format
 ```
---
Either **`--public`**, **`--private`** or **`--internal`** flags **are required** when not running interactively.

# Show remotes (.git origins)
```
git remote -v
```
