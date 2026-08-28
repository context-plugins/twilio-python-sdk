<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConversationsV1DeliveryReceipt — operations

Accessor: `client.conversations_v1_delivery_receipt` · Source: `twilio_sdk/apis/conversations_v1_delivery_receipt.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations_v1_delivery_receipt.fetch_conversation_message_receipt

- **Route**: `GET /v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_conversation_message_receipt(conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `message_sid`, `sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `message_sid` — path `MessageSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ConversationsV1ConversationConversationMessageConversationMessageReceipt`
- **Returns (raw)**: `ApiResult[ConversationsV1ConversationConversationMessageConversationMessageReceipt, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ConversationsV1ConversationConversationMessageConversationMessageReceipt` | `twilio_sdk/models/conversations_v1_conversation_conversation_message_conversation_message_receipt.py` |

### client.conversations_v1_delivery_receipt.fetch_service_conversation_message_receipt

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}`
- **Server**: `default7`
- **Signature**: `def fetch_service_conversation_message_receipt(chat_service_sid: str, conversation_sid: str, message_sid: str, sid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `message_sid`, `sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `message_sid` — path `MessageSid` · `sid` — path `Sid`
- **Returns (parsed)**: `ServiceConversationMessageReceipt`
- **Returns (raw)**: `ApiResult[ServiceConversationMessageReceipt, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ServiceConversationMessageReceipt` | `twilio_sdk/models/service_conversation_message_receipt.py` |

### client.conversations_v1_delivery_receipt.list_conversation_message_receipt

- **Route**: `GET /v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts`
- **Server**: `default7`
- **Signature**: `def list_conversation_message_receipt(conversation_sid: str, message_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `conversation_sid`, `message_sid`
- **Params**: `conversation_sid` — path `ConversationSid` · `message_sid` — path `MessageSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListConversationMessageReceiptResponse`
- **Returns (raw)**: `ApiResult[ListConversationMessageReceiptResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListConversationMessageReceiptResponse` | `twilio_sdk/models/list_conversation_message_receipt_response.py` |

### client.conversations_v1_delivery_receipt.list_service_conversation_message_receipt

- **Route**: `GET /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts`
- **Server**: `default7`
- **Signature**: `def list_service_conversation_message_receipt(chat_service_sid: str, conversation_sid: str, message_sid: str, *, page_size: int | None = None, page: int | None = None, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chat_service_sid`, `conversation_sid`, `message_sid`
- **Params**: `chat_service_sid` — path `ChatServiceSid` · `conversation_sid` — path `ConversationSid` · `message_sid` — path `MessageSid` · `page_size` — query `PageSize` · `page` — query `Page` · `page_token` — query `PageToken`
- **Returns (parsed)**: `ListServiceConversationMessageReceiptResponse`
- **Returns (raw)**: `ApiResult[ListServiceConversationMessageReceiptResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListServiceConversationMessageReceiptResponse` | `twilio_sdk/models/list_service_conversation_message_receipt_response.py` |

