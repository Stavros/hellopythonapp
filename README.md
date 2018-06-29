S2I example usage with a Python sample app
==========================================

S2I, Source-To-Image, is a toolkit for building Docker images with minimum effort. You can use S2I to generate a docker image including your code changes.

## Clone this repo locally

```
git clone https://github.com/Stavros/hellopythonapp.git
```

## Create an OepnShift application

```
oc new-app . --name=mypythonapp
```

## Create a S2I build-hook

```
oc set build-hook bc/mypythonapp --post-commit --script="py.test"
```

## Licence

Forked project. Copyright (c) 2018 Stavros Kalapothas (aka Stevaras) <stavros@ubinet.gr>.
It is free software, and may be redistributed under the terms of the GNU Licence.