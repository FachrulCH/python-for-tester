# Install Chromedriver
In mac:
```shell
brew install --cask chromedriver
brew upgrade --cask chromedriver
```

If found error
`Error: “chromedriver” cannot be opened because the developer cannot be verified. Unable to launch the chrome browser`

Then do `xattr -d com.apple.quarantine $(which chromedriver)`
