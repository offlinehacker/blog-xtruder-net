Goodbye pyramid, hello loopback!
################################

:date: 2014-09-22 01:08
:tags: pyramid, loopback, strongloop, rest, api
:category: dev
:slug: pyramid_2_loopback
:summary: How migration of rest api from pyramid to loopback made my life a lot
          easier

Intro
-----

There are times in your life when you have to make a decision to change
something, and yeah as we all know it can be sometimes hard, especially if
you are not the only person who is affected by changes.

I am python enthusiast and the first framework i used for web
development was `pyramid
<http://www.pylonsproject.org/projects/pyramid/about>`_. Pyramid is great, it allows very easy for developer to
create arbitary web application. A year ago i created backend for application
called `euganke <http://euganke.fri.uni-lj.si/>`_ and i must admit that this
was my first web application.

Pyramid allowed me to prototype really quickly
and create results i wanted, but as code got bigger and bigger, it became
clear that pyramid was not a good decision for an rest api framework, mostly
dealing with reading and writing data to database models. This was
primarily because i had to write all this basic stuff like login,
authentication, verification, password reset by myself. I also had custom
implementation for doing queries, custom generators for api docs, and custom 
schema helper decorators for enforcing security. I could devote more time in
perfecting this stuff, but this was not my life goal, i wanted to have
framework that has these basic things built in and is also nice to frontend developers.

A journey to node(js)land
-------------------------

So that's where a journey started, in an attempt to chase my perfect framework
for doing rest api-s. Because i'm primarilly python programmer, i looked on
field of non django python frameworks, i just didn't want to learn django to
make this not so complicated rest appliacation.

I found
`python-eve.org <python-eve.org>`_ and it started to look really promissing, 
when i realized you only need to speciffy a schema and data is automatically
exposed, and it had authentication and a basic seucirty built in, but it turned
out that secuirty interfaces they had, were too basic, and design was not the
best, so after a few hours reading a source code i decided to take another try.

.. image:: |filename|/images/eve-sidebar.png
    :width: 50%
    :target: http://python-eve.org 

Because i was not able to find anything similar, but better in python i decided
to look for another languages. We had frontend already written in javascript,
with all these cool technologies like nodejs, bower, grunt,... so i asked mysef
why not nodejs. For those who don't know nodejs is server side javascipt engine
based on google's V8, so it has all the speed your browser has, but on
serverside. After some googling araound i found `loopback
<http://loopback.io/>`_. When i first saw it i just looked like a pure
framework of rest awesomeness.

.. image:: |filename|/images/loopback_logo.png
    :width: 20%
    :target: http://loopback.io


Loopback
--------

Loopback is a node.js rest framework based on express, which allows you 
to simply create dynamic
rest api-s. The idea is, instead of trying to write code for every rest
endpoint, and query data from database, you simply define models with all
the properties, relations and access control list in a simple json file.
Loopback was designed with support for mobile applications, has data 
connectors for all major databases and is super extendable. 

Let me give you example how simple it is to create project and add data models:

- **scaffold**::

    $ npm install -g generator-loopback
    $ yo loopback

         _-----_
        |       |    .--------------------------.
        |--(o)--|    |  Let's create a LoopBack |
       `---------´   |       application!       |
        ( _´U`_ )    '--------------------------'
        /___A___\
         |  ~  |
       __'.___.'__
      ´   `  |° ´ Y `

    [?] Enter a directory name where to create the project: .
    [?] What's the name of your application? todo

- **create a new model using yo**::

    $ yo loopback:model
    [?] Enter the model name: todo
    [?] Select the data-source to attach todo to: db (memory)
    [?] Expose todo via the REST API? Yes
    [?] Custom plural form (used to build REST URL):
    Let's add some todo properties now.

    Enter an empty property name when done.
    [?] Property name: title
    invoke   loopback:property
    [?] Property type: string
    [?] Required? Yes

    Let's add another todo property.
    Enter an empty property name when done.
    [?] Property name: owner
    invoke   loopback:property
    [?] Property type: object
    [?] Required? No

- **extend model with acl definitions in `common/models/todo.json`**::

    {
        "name": "todo",
        "base": "PersistedModel",

        ...

        "acls": [
        {
            "accessType": "*",
            "principalType": "ROLE",
            "principalId": "$everyone",
            "permission": "DENY"
        },
        {
            "accessType": "*",
            "permission": "ALLOW",
            "principalType": "ROLE",
            "principalId": "admin"
        },
        {
            "accessType": "WRITE",
            "permission": "ALLOW",
            "principalType": "ROLE",
            "principalId": "$owner"
        },
        {
            "property": "create",
            "permission": "ALLOW",
            "principalType": "ROLE",
            "principalId": "$everyone"
        }
        ]
    }

- **put additional logic to `server/models/todo.json`**::

    module.exports = function(Todo) {

      // Set group owner
      Todo.beforeRemote('create', function(ctx, todo, next) {
        var body = ctx.req.body;

        if (ctx.req.accessToken) {
          body.owner = ctx.req.accessToken.userId;
        }

        next();
      });

    };

- **server the project**::

    $ node .
    Browse your REST API at http://localhost:3000/explorer
    Web server listening at: http://localhost:3000/

You have just created a new service with todo model, with enabled
authentication, registration, security and awesome **api explorer** for
debugging and testing, how awesome is that.

.. image:: |filename|/images/loopback_explorer.png

Loopback in practice
--------------------

After a few months of using loopback i can say that it literally reduced
codebase on our project by a few magnitudes, and it made my life a lot
easier. We are using loopback with mongodb, and without orm, requests are
processed in range of a few milliseconds. Because it's based on express you
can pretty much use any of the express plugins.

Loopback is currently on
version 2.2 and it still has many bugs, so i had to fix or monkey patch some of
them to make different features work as they should, but i can live with that.
It turns out codebase is quite nicely
readable for javascript, so fixing and adding new features is really not an
issue. Framework is still in development, so documentation is not
up-to-date, but you have github, and maintainers really do a good job,
responding to issues.

**So at the end, one more happy programmer, with less code to maintain, but let's
see what happens when we launch a new version of our project ;)**
