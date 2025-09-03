"Package.json"
packages with **~** = latest **PATCH**, example:
>"~1.1.3", will keep update to any **1.1.x** patch.

packages with ^ = latest MINOR, example:
> "^1.1.3", will keep update to any **1.x.x** patch.

///////////////////////////////////

**METHOD 1 using : function(req, res){};**
app.get("/", function(req, res) {
    res.send('Hello Express METHOD 1');
  }
)

**METHOD 2 using : (req, res) => {};**
app.get("/", (req, res) => {
    res.send('Hello Express METHOD 2');
  }
)

# Regex
Regex syntax = "/[regex]/"
Regex can be defined using backslash "\\" + desired regex
#### "/g" is used to set global regex.
```
 /[regex]/g
```
#### "/i" is used for insensitive.
```
/[regex]/i
```
#### "\\s" is used for whitespaces.
```
 /[\s]/
```
#### "\\d" is used for digits.
```
/[\d]/
```
### Example of Regex removing plus(+), minus (-), whitespaces (\\s), and in global setting (/g):
 ```
function cleanInputString(str) {
  console.log("original string: ", str);
  const regex = /[+-\s]/g;
  return str.replace(regex, '');
}
console.log(cleanInputString("+-99"));
```
#### Output:
original string: +-99
99