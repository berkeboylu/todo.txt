## Actions

### `add`
Adds THING I NEED TO DO to your todo.txt file on its own line.  

Project and context notation optional.  

Quotes optional.

```shell
t add "THING I NEED TO DO +project @context"
t a "THING I NEED TO DO +project @context"
```

### `append`
Adds TEXT TO APPEND to the end of the task on line ITEM#.

Quotes optional

```shell
t append ITEM# "TEXT TO APPEND"
t app ITEM# "TEXT TO APPEND"
```

### `list`
Displays all tasks.
​    
```shell
t list [TERM...]
t ls [TERM...]
```

### `listpri`

Displays all tasks prioritized PRIORITIES. If no PRIORITIES specified, lists all prioritized tasks.

```shell
t listpri [PRIORITIES]
t lsp [PRIORITIES]
```