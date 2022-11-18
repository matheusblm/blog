#### Avoid Nesting when you're Testing

Basic u jest write a describe with it, when ins necessary.
When the tests are no related you can write with Test sintax.

### Redis vs Kafka vs RabbitMQ

This three are broker ensures comunnications bettween different microservices.

Async and Sync commnucatition on microservices, u can wait for a response before send the next message, or the next message is send without the response.

RabbitMQ (AMQP)
Scale: based on configuration and resources, the ballpark here is around 50K msg per second.

Persistency: both persistent and transient messages are supported.

Kafka
Scale: can send up to a million messages per second.

Persistency: yes.

Redis
Scale: can send up to a million messages per second.

Persistency: basically, no — it’s an in-memory datastore.
