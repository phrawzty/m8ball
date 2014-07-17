# Magic 8-Ball
This is an API for the Magic 8-ball service. It is a Flask app built using the [Flask Restful](http://flask-restful.readthedocs.org/en/latest/) library; you will need to have that package (and its dependencies) available.

## WARNING WARNING WARNING
This is just a mock-up and is primitive like the stone age. Expect all sorts of things to change.

# Runtime configuration
All runtime configuration is set via environment variables. These variables must be prefixed with `M8_`.

## Debug
To enable _debug_ mode just set the `M8_DEBUG` environment variable to `true`, for example:
```
$ /usr/bin/env M8_DEBUG=true python ./runserver.py
```
Don't do this in production.

## AWS
AWS interaction is supplied by the Boto library, therefore credentials must be specified in a [Boto-appropriate manner](http://boto.readthedocs.org/en/latest/boto_config_tut.html#credentials).
```
M8_AWS_ACCESS_KEY_ID=<key>
M8_AWS_SECRET_ACCESS_KEY=<secret>
```
These are only required if AWS is actually being used.

## Data stores (back-end)
Sources for the UUID and API key store must also be specified.
```
M8_UUID_SOURCE=<bucket>
M8_AUTH_SOURCE=<bucket>
```
In the case of AWS these would be the respective bucket names. For the pretend backend (see below) they would be files.

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

## S3Backend
This is a simple abstraction layer for reading and writing keys from an S3 bucket. It extends `get` and `set` methods; in the latter case, note the `clobber` option above.

## PretendBackend
This can be used in the place of a "real" key/value backend (useful for off-line development). It accepts a JSON file as input (instantiation), and extends `get` and `set` methods just like a real k/v store. It does not write to disk.

## AuthBall
There are a number of potential options for authentication. This class aims to act as an abstraction layer to those options. Currently the only implemented mechanism is a simple API key. I'd like to add a PKI mechanism down the line as well.
