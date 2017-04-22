Asset Store Coding Challenge
============================

The doves are loose and lots of other satellites are showing up to the party. Antennas to communicate with the ever expanding fleet are popping up like wildflowers. To keep track of them all, we need an asset store. We've already worked out the initial requirements and made a few design decisions:

- The asset store is going to be exposed as a custom RESTful web API written in python.

- Every asset that we store has an "asset name". There are some rules about asset names:
  - They must be globally unique across all assets
  - They can only contain alphanumeric ascii characters, underscores, and dashes
  - They cannot start with an underscore or dash
  - They must be between 4 and 64 characters long

- Every asset has an "asset type" which is a string that must either be "satellite" or "antenna".

- Every asset has an "asset class" which depends on its asset type and is a string. For "satellite" assets it can be "dove" or "rapideye". For "antenna" assets it can be "dish" or "yagi".

- Users can create assets. To do so, they must supply the asset name, asset type, and asset class.

- Users can retrieve the whole list of assets.

- Users can retrieve a single asset by name.

- An asset cannot be deleted. Also its name, type, and class cannot be changed.


Implementation Notes:
---------------------

Any design decisions not specified herein are fair game. Completed projects will be evaluated on how closely they follow the spec, their design, and cleanliness of implementation.

Completed projects must be delivered in a git repo (or similar) available to the reviewer.

Completed projects must include a README with enough instructions for evaluators to build and run the code. Bonus points for builds which require minimal manual steps.

This project should not take more than 3-4 hours to complete. Do not get hung up on scaling or persistence issues. This is a project used to evaluate your design and implementation skills only.

Please include any unit or integration tests used to verify correctness.

Extra Credit
------------

You are not expected to spend more than 3-4 hours on this exercise. Indeed, you may not even need that much time. But here are some ideas if you want to go bigger:

- Implement "asset details". Every asset has "asset details". This is a list of key/value pairs that describe the asset. The list of expected/acceptable key/value pairs depends on the asset class. Specifically:

    - dish: dishes have a "diameter" key whose value is a float and a "radome" key whose value is a boolean.
    - yagi: yagis have a "gain" key whose value is a float.

  Users can set the details of an asset.

- Require an X-User header that is set to the username. The user can only create assets if their name is admin. Don't worry about actually implementing some kind of authentication scheme. Just use the header if it's available.

- Implemenet filtering. When a user specifies an asset_class or asset_type to the "whole list of assets" feature, the returned list should be appropriately filtered.
