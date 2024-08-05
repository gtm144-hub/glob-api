## Glob Test API

This API aims to apply the code challenge sent by e-mail. Given the time constraints, I would resolve this challenge in three phases:

### Phase 1:
Solve the two sections in a simple manner given the following characteristics:

- Use the main branch only
- Create docker compose for fast-api app and postgress db
- Create manual unit tests for pytest
- Add postman workplace api tests

### Phase 2:
- Create continous development(cd) with github actions to run test automatically 
- Deploy app to GCP cloud run

### Phase 3:
- Add error messages
- Add optimization techniques:
-- For high concurrency, look for multithready solutions (dask)
-- For large csvs, take generators into consideration with sqlalchemy
