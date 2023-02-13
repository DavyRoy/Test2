
**Genesis Proxy Gateway (gpg) service**  
  
Combine in itself all this  the services: 
 - user-api 
 - document-api 
 - task-api  
 - FEATURES(project-api, agreement-api, etc.)
---
**BEFORE LAUNCHING CHECK THAT YOU HAVE THE RELATED SERVICES RUNNING**  
 
- Rabbit mq
- - run command **in Gpg_api** `docker-compose up --build -d rabbitmq`
- KeyDB
- - run command **in Gpg_api** `docker-compose up --build -d keydb`
- User-api 8001 port  
- - run command **in User-api** `docker-compose up --build user_api`
- Document-api 8002 port  
- - run command **in Document-api** `docker-compose up --build document_api`
- Task-api 8003 port   
- - run command **in Task-api** `docker-compose up --build task_api`
  
**ALSO CHECK THAT YOU HAVE SETUP AUTH TOKENS FOR SERVICES**   
- add in *src/gpg_api/settings/local*  
- - **USER_API_TOKEN** = 'you token here'  
- - **DOCUMENT_API_TOKEN** = 'you token here'  
- - **TASK_API_TOKEN** = 'you token here'

**AND NOW YOU READY TO UP GPG**
Run command **in Gpg_api**-> `docker-compose -f docker-compose.yml up --build gpg_api`

---
**TO ACCESS ADMIN PANEL ANY OF THIS SERVICE USE AUTO GENERATED SUPER-USER**
Username: `root` by default
Password: `root` by default