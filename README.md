# µtrello

## Installation

You can use Docker or pip.

Using pip: `pip install utrello`

Using docker: `docker run ghcr.io/davividal/utrello:master`

## Usage

From the CLI:

```bash
utrello --help
usage: utrello [-h] [--api_key API_KEY] [--api_token API_TOKEN] {boards,lists,cards} ...

Interacts with Trello Restful API

positional arguments:
  {boards,lists,cards}  service help

optional arguments:
  -h, --help            show this help message and exit
  --api_key API_KEY
  --api_token API_TOKEN
```

You can get your own Trello API key at https://trello.com/app-key . After that, generate a manual token, in the same page. You need to provide both values in order to use this program.

You can provide the credentials either as arguments or via environment variables: `TRELLO_API_KEY` and `TRELLO_API_TOKEN`.

## Implemented features

Currently the implemented features are: list all board for the current user, list all lists for a given board and create card for a given list.

In order to create a card, the workflow is the following:

```bash
$ utrello --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN boards list
# ...
$ utrello --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN lists --board_id BOARD_ID_FROM_PREVIOUS_OUTPUT
# ...
$ utrello --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN cards create --name test --idList LIST_ID_FROM_PREVIOUS_OUTPUT
```

## Creating cards in batch

If you with to create multiple cards at the same time, you can do so using a CSV. The order of the columns is irrelevant.

The format must be like this:

```csv
idList,name,desc
list_id_1,task 1,test task 1
list_id_2,task 2,test task 2
list_id_1,task 3,test task 3
```
Note that you can create cards for whichever list you want.

### Using Docker

If you want to create cards using CSV under Docker, you can simply use volumes for that:

```bash
docker run -v $PWD/cards.csv:/cards.csv:ro ghcr.io/davividal/utrello:master --api_key YOUR_API_KEY --api_token YOUR_API_TOKEN cards create -f /cards.csv
```
