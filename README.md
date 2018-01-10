# EveCherryPrevent

Bored about mining drama in your corp/alliance ?

This tool will help you find those people who are only doing cherry picking !
You can doing mining ladder board, and adapt your mining rules with it !

## How does it work ?

  It computes a reward quantity from extracted values you picked from EVE Client API. It also computes an ore distribution from average ore quantity in anomalies belt.

  Default cherry ORE values : 'Arkonor', 'Bistot', 'Gneiss', 'Crokite'.

  Default dirty ORE values : 'Dark Ochre', 'Spodumain', 'Mercoxit'.

  So, if you extract the belt average Ore quantity your reward will be 0 (Belt cleaner), if you extract too many cherry ores your reward will be < 0 (Bad miner, likely to be cherry picking), and if you extract only dirty ores your reward will be > 0 (Good miner !)
