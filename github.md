# LikeLion github session

### git
1. create Git Repository
2. git init
3. git remote add origin (repo_address)
4. git add --all
5. git commit -m ("info")
6. git push origin master / force = git push -f origin master

git branch (branchname) : 새로운 브런치 생성
git checkout (branchname) : 해당 브랜치로 이동
git pull origin (branch) : 원격 저장소의 특정 브랜치에서 변경사항 pull

-------------------------------------------------------------------------

### Github을 이용한 협업

1. 원격 저장소 생성
2. 팀원을 Collaborator로 추가
3. 초기 프로젝트 push
4. 팀원들의 로컬에 프로젝트 pull
5. 팀원 각자의 브랜치를 생성하여 작업
6. 브랜치에 작업한 내용을 push
7. Master와 merge 하기 전 Pull request
8. Pull request 확인 후 Master와 merge

### Fork를 이용한 협업

1. 작업하고 싶은 Repository fork 해오기
2. 자신의 로컬에서 작업
3. 변경사항을 자신의 브랜치에 push
4. 원본 레포지토리 소유자에게 Pull request 요청
5. 소유자가 Pull request를 승인하여 merge 하면 자동으로 Collaborator 추가