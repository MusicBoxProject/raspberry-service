# raspberry-service

A Kinto plugin to start/stop playing a playlist on MPD.

JSON schema:

```json
{
  "properties": {
    "status": {
      "title": "Status",
      "type": "string",
      "description": "Is the tag on currently on the reader?",
      "enum": [
        "on",
        "off"
      ]
    },
    "nfcReader": {
      "title": "NFC Reader ID",
      "type": "string",
      "description": "The ID of the NFC reader that did the update"
    }
  },
  "type": "object"
}
```

UI schema:

```json
{
  "ui:order": [
    "nfcReader",
    "status"
  ]
}
```
