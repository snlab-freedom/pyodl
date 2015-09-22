# Logging

This library uses python logging module. If you would like to see debug messages
please see the file `settings/logging.conf`. This file is at this repository just for
convenience.

To enable DEBUG logging during the execution of sample scripts, edit the section
`logger_odl` in your `settings/logging.conf` :

```
[logger_odl]
level=DEBUG
handlers=ConsoleHandler
qualname=odl
propagate=0
```

*NOTE*: You should not commit changes on this file.
