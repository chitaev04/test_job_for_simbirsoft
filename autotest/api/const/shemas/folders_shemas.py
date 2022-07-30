schema_create_folder = {
  "type": "object",
  "properties": {
    "href": {
      "type": "string"
    },
    "method": {
      "type": "string"
    },
    "templated": {
      "type": "boolean"
    }
  },
  "required": [
    "href",
    "method",
    "templated"
  ]
}