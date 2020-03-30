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

- **git checkout -t 원격저장소branch이름**   
-t 옵션과 원격저장소의 branch이름을 입력하면 로컬의 동일한 이름의 branch를 생성하면서 해당 branch로 checkout   

- **git checkout -b 새로만들 브랜치 분기될 브랜치**   
새로운 브랜치를 생성(브랜치 추적)   
   
하위 브랜치와 상위브랜치 병합   
 -1 **git checkout 원격저장소branch이름**   
 -2 **git merge 로컬저장소**   
 -3 **git push origin 원격저장소이름**   


