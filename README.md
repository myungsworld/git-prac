## 깃허브 사용법 및 명령어

[깃허브참조사이트](http://www.talkdev.net/git-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%82%AC%EC%9A%A9%EB%B2%95/)   
[마크다운문법참조사이트](https://heropy.blog/2017/09/30/markdown/)
### 개념

+ **브랜치**:Git에서는 저장소가 처음 만들어지면 마스터(master)브랜치가 생성되고 이 브랜치에서 기본적인 버전관리가 진행된다.새로운 기능을 추가하는 작업은 새로운 브랜치를 만들어 작업을 수행하며, 작업이 정상적으로 마무리되면 작업 내역을 마스터 브랜치에 병합한다. 이렇게 마스터 브랜치와 별도로 생성하는 브랜치를 토픽(topic) 브랜치 또는 피처(Feature) 브랜치라 한다. 각각의 브랜치는 다른 브랜치에 영향을 주지 않으므로 독립적인 여러 작업을 동시에 진행 할 수 있다.

+ **스테이징 영역**: 작업 내용을 한번 더 확인하여 선별적으로 지역 저장소에 반영하기 위함 시간이 소요되지만 좀더 안정적임
### 명령어
- **git init**   
지역 저장소 생성   

- **git status**   
파일 상태 확인하기   

- **git remote add origin 원격저장소위치(https://~)**   
지역 저장소와 원격 저장소의 첫번째 실제 연결 만들기   

- **git remote -v**   
확인을 위한 명령어   
이 명령어는 로컬 저장소가 알고있는 원격 origin에 대한 모든 항목을 보여준다.   
지금까지 함께 하였다면,단 하나이어야 한다. 두 개가 리스트된 것은 정보를 push하고 fetch할 수 있는 것을 뜻한다

- **git remote set-url origin 변경할 위치(https://~)**   
원격 저장소를 변경할때 사용하는 명령어 리포지터리를 바꿀때 사용    

- **git add filename**   
작업 내용을 지역 저장소에 저장하기 위해 **스테이징 영역(staging area)** 에 추가   

- **git commit -m "filename"**   
commit은 작업 내역을 지역 저장소에 저장, -m 플래그는 뒤따르는 텍스트는 메시지로 읽는다   
커밋 메세지가 현재형이므로 시간에 대한 유연성을 가지므로 현재형으로 작성한다   

- **git commit --amend -m "변경할 메시지"**  
직전 커밋의 메시지 만을 수정  

- **git push**   
로컬 저장소의 변경 내역을 원격 저장소에 반영한다.   
 > //fatal: The current branch master has no upstream branch. 브랜치가 원격저장소에 없을경우 발생   
 > 두가지 해결방안 **git push -u origin master** 혹은 **git push -f origin master**   
  

- **git push origin master**   
master branch에 push한다.   
> ! [rejected]        master -> master (fetch first) 이미 변경된 파일이 원격저장소에 있을경우 발생   

- **git pull origin master**   
원격저장소의 내용을 가져와 로컬저장소의 내용과 자동으로 병합작업을 수행한다.


- **git rm filename**   
원격저장소에 있는 파일을 삭제하기 위해서 사용되는 건데 cmd창에서도 git bash here에서도 실행되지 않는다 원인을 모르겠다   
git rm -rf filename 안되면 이렇게 해보라는데 이것도 안되고   
git rm -r --cached filename filename 여러개를 동시에 지우는것도 안된다   
cmd창에서 파일을 삭제하고 싶다 물론 깃허브에서 delete this file을 누르면 삭제되긴 하는데 간지가 나지않는다   

- **git branch -a**   
원격 브랜치와 로컬 브랜치 리스트 모두 보여줌

- **git push origin --delete <원격저장소 branch이름>**  
로컬에서 원격 브랜치 삭제  

- **rm -rf .git**  
nodejs 리포에 study라는 폴더가 있었는데 내용물을 바꾸고 커밋을 해도 인식이 안되서 고생하다가 history가 상관이 없다면 저렇게 하라고 해서 함  
분명 인식이 안되는 이유가 있을텐데 왜 그런지 구글링을 해봐도 답을 찾지 못했다.  

- **git branch [브랜치이름]**  
현재 분기 유지하면서 새 분기 만듬  

- **git checkout -t 원격저장소branch이름**   
-t 옵션과 원격저장소의 branch이름을 입력하면 로컬의 동일한 이름의 branch를 생성하면서 해당 branch로 checkout   

- **git checkout -b 새로만들 브랜치 분기될 브랜치**   
새로운 브랜치를 생성(브랜치 추적)   
   
하위 브랜치와 상위브랜치 병합   
- **1git checkout 원격저장소branch이름**   
- **2git merge 로컬저장소**   
- **3git push origin 원격저장소이름**   
---
- **git fork [git URL]**  
- **git clone [복사된 URL]**  
- **git remote add upstream [git URL]**
협업할 레포를 내 레포로 추가, 로컬저장소에 복제, 새로운 원격저장소 remote 추가 (upsteam 권장), 작업후 push 하면   
upstream 쪽 협력자가 pull request 를 할지 결정  

- **git fecth upstream**
- **git merge upstream/master**  
upstream 변경 내역 확인, upstream 저장소의 마스터 브랜치를 우리의 프로젝트에 병합하겠다는 의미   

- **clone과 fork의 차이**   
타인의 저장소를 가져오는 방법 중에 가장 처음 접하는 방법은 보통 클론이다.  
클론을 하는 경우, 타인의 저장소에 대한 변경 권한이 없다.  
커밋은 가능하지만 푸시를 할 경우 Permission denied라는 에러 메세지가 나오며 거절되는 것을 볼 수 있다.  
이를 해결하는 방법 중 첫 번째는 깃허브 저장소에서 collaborator에 내 계정을 등록하는 방법이다.   
해당 저장소에 대해 푸시를 할 수 있는 권한을 얻게 되는데, 이런 경우 아래와 같은 문제가 발생할 수 있다.  
협업의 과정에서 브랜치와 커밋에 대한 규정을 지켜놓고 철저하게 따른다면 문제가 생기지 않겠지만   
모든 팀원이 오리지널 저장소에 대한 모든 권한을 갖게 되는건 바꿔 말하면 누구나 오리지널 코드를 망칠 수 있다는 것이다. 
잘못된 내용을 커밋하는 경우,  
지우지 말아야 할 내용을 지우는 경우 등의 위험을 내포한다.   
두 번째 방법은 오리지널 저장소를 팀원 각각이 포크하여 사용하는 방법이다.   
포크된 저장소에 대한 권한은 나에게 있고, 이 때는 푸시에서 퍼미션 문제가 생기지 않는다.   
팀원들은 본인의 저장소에 작업한 내역을 커밋하고 푸시하며 오리지널 저장소에 병합을 요청한다.   
오리지널 저장소의 권한을 가진 사람은 병합 요청을 확인하고 문제가 없을 때 병합을 승인하면 된다.   

- **git submodule add [추가할 URL]**  
내 깃 저장소에 다른 깃 저장소를 디렉토리로 분리해 넣는 것    
각 저장소의 커밋을 독립적으로 관리한다.  

- **git reset --soft HEAD^**  
commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉토리에 보존  

- **git reset --mixed HEAD^**  
commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉토리에 보존  

- **git reset --hard HEAD^**  
commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉토리에서 삭제  
이거 하지마셈 커밋한거 다 사라짐 ㅋㅋ루삥뽕  

- **.ignore**  
root directory에 .env안에 있는 파일이나 node_modules 같은 대용량 파일 무시해주는 용도  
중요한 내용 프라이빗 키 같은 경우를 깃허브 올리는것 방지  
ignore 파일이 먹히지 않을 경우  
git rm -r --cached .  
git add .  
git commit -m "fixed untracked files"  



깃 이그노어 깃 로그에 깃 리베이스 정리
