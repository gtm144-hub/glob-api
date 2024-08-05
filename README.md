## Glob Test API

This API aims to apply the code challenge sent by e-mail. 

## Development
Given the time constraints, I would resolve this challenge in two phases:

### Phase 1:
Solve the two sections in a simple manner given the following characteristics:

- Use the main branch only
- Create docker compose for fast-api app and postgress db
- Create manual unit tests for pytest
- Add postman workplace api tests

### Phase 2:
- Create continous development(cd) with github actions to run test automatically 
- Deploy app to DigitalOcean Droplet

## Local Deployment

1. Clone this repository
1. Install docker-compose
2. Run docker-compose up inside repo
3. Use Postman collection to test API, use http://local-host:8070 as base_url

## Developer Notes
- In upload data endpoints, chuncks of 1Mb were used to ingest information to the database because the csv data shouldn´t overload the memory. Transactions will increase as the file gets bigger but the memory in API should be safe.
- GCP Cloud Run was first intended to use but given that the local docker development uses volumes is not suited for stateless application. In this case, cloud SQL should replace the Postgres container and run API app in Cloud Run. In this manner, database and API could scale with GCP help.
- Pandas was best suited to serialize and deserialize the processing data inside API app in comparison to for loops. Code is faster, cleaner and concise.
