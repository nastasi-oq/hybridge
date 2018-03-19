# hybridge

The purpose of this add-on is create a as much as possible reusable infrastructure to connect third-party application with the browser (without embed it as Qt do with old webkit versions) extending web-application capabilities when the application is ready to interact with the browser.

## Chrome

### Web-side examples
copy or place a link to the `chrome/web` in your webserver directory tree.

## Add-on

Copy `chrome/manifest.json.tmpl` to `chrome/manifest.json` and change matches accordingly with the webserver path.

You must register the add-on passing the `chrome` directory to the chrome add-on manager.

## API interface

### Call remote method

call('method_name', callback_hdl, arguments ... )

`callback_hdl` is of type function callback_hdl(reply_message) where

`reply_message` has { '`complete`': true/false // set to false to return progress info
              '`ret`': any // the content returned by the call
             }


### Called local method

method_name(send_response_cb, uniq_id_call, arguments ... )

`send_reply_cb` is of type function send_reply_cb(`uniq_id_call`,
    `reply_message`)

if the `reply_message` is partial set `complete` to `false`.

