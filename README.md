# named_entitiy_recognition
You can create your own text dataset for Named Entitiy Recognition (NER) for your project with this package. I created a minor dataset as an example from 10 news website.


# you should have
- bs4
- spacy
- os
- requests

# input
- URL list (I added example URL list which I created based on popular English news websites.

# outputs
- html dataset in a directory you specified
- a list of dictionaries. each dictionary has three keys-values:
-- "filename" + "text data of the file" + "entity tuples as text-label";
