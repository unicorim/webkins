
  # ==Napkin==
  # @name           Say Hello!
  # @namespace      https:/github.com/<url>
  # @description    Greets the world
  # @include        http://google.com/*
  # @include        http://facebook.com/*
  # @exclude        http://yahoo.com/*
  # @render         hello
  # ==/Napkin
  # Notes:
  #    * is a wildcard character
  #    Nobody likes yahoo ;)
  
  # For the moment, we only allow web remixes. Nothing fancy
  # like altering DOM. No sir, we still have a lot to go 
  # before we tame that hackasaurus yet!

  @@ hello
  <!DOCTYPE html>
  <html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Says Hello</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">
    </head>
    <body>
        <p>Hello world!</p>
    </body>
  </html>
