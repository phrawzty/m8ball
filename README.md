# Magic 8-Ball
This is an API for the Magic 8-ball service.

## WARNING WARNING WARNING
This is just a mock-up and is primitive like the stone age. Expect all sorts of things to change.

# Details, details
This is a Flask app built using the [Flask Restful](http://flask-restful.readthedocs.org/en/latest/) library; you will need to have that package (and its dependencies) available.

## Debug
To enable _debug_ mode just set the `M8_DEBUG` environment variable to `true`.
```
$ /usr/bin/env M8_DEBUG=true python ./runserver.py
```
Don't do this in production; actually, don't run this in production at all (debug or no).

# API
There is only one useful endpoint: `/uuid/`

## `/uuid/`

### `GET`
One or more UUIDs can be, er, GETted at a time:
```
/uuid/<UUID>[,UUID]
```

### `PUT`
One UUID can be PUT at a time:
```
/uuid/<UUID>
```

It is necessary to authenticate for PUT requests. Currently the only auth mechanism is an API key (see `api_key` below).

### Options
There are some options that can be passed to the `/uuid/` endpoint. These options can either be specified in the URL directly, or as form encoded elements.
```
$ curl 'http://<serv>/uuid/<uuid>?empty=true'
$ curl 'http://<serv>/uuid/<uuid>' -d 'empty=true'
```

#### `empty`
Return empty results.

Default: _false_

#### `clobber`
Overwrite an existing UUID during PUT.

Default: _false_

#### `api_key`
Pass an API key.

Default: _none_

# Under the bonnet

## PretendBackend
Since we don't know what actual datastore(s) we're going to use, there is a make-believe datastore called _PretendBackend_. It accepts a JSON file as input (instantiation), and extends `get` and `set` methods just like a real key/value store. It does not write to disk.

## AuthBall
Since we don't know what actual authentication mechanism(s) we're going to use, there is a primitive class called AuthBall that could - in principle - be used to abstract different auth possibilities. I'm not sure if this is something we need or want (yet).