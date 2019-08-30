#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-apache-rat
Version  : 0.11
Release  : 9
URL      : https://github.com/apache/creadur-rat/archive/apache-rat-project-0.11.tar.gz
Source0  : https://github.com/apache/creadur-rat/archive/apache-rat-project-0.11.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.pom
Source3  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.jar
Source4  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.pom
Source5  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-project/0.10/apache-rat-project-0.10.pom
Source6  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-project/0.6/apache-rat-project-0.6.pom
Source7  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.jar
Source8  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.pom
Source9  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.jar
Source10  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.pom
Source11  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat/0.10/apache-rat-0.10.jar
Source12  : https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat/0.10/apache-rat-0.10.pom
Source13  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar
Source14  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom
Source15  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.jar
Source16  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.pom
Source17  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar
Source18  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom
Source19  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.jar
Source20  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.pom
Source21  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar
Source22  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom
Source23  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-project/0.11/apache-rat-project-0.11.pom
Source24  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom
Source25  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.jar
Source26  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.pom
Source27  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.11/apache-rat-0.11.jar
Source28  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.11/apache-rat-0.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-apache-rat-data = %{version}-%{release}
Requires: mvn-apache-rat-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

%package data
Summary: data components for the mvn-apache-rat package.
Group: Data

%description data
data components for the mvn-apache-rat package.


%package license
Summary: license components for the mvn-apache-rat package.
Group: Default

%description license
license components for the mvn-apache-rat package.


%prep
%setup -q -n creadur-rat-apache-rat-project-0.11

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-apache-rat
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-apache-rat/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-apache-rat/NOTICE
cp apache-rat-core/src/test/resources/elements/LICENSE %{buildroot}/usr/share/package-licenses/mvn-apache-rat/apache-rat-core_src_test_resources_elements_LICENSE
cp apache-rat-core/src/test/resources/elements/NOTICE %{buildroot}/usr/share/package-licenses/mvn-apache-rat/apache-rat-core_src_test_resources_elements_NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.10
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.10/apache-rat-project-0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.6
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.6/apache-rat-project-0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10/apache-rat-0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10/apache-rat-0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.11
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.11/apache-rat-project-0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11/apache-rat-0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11/apache-rat-0.11.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.10/apache-rat-core-0.10.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.11/apache-rat-core-0.11.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.6/apache-rat-core-0.6.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.11/apache-rat-plugin-0.11.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.10/apache-rat-project-0.10.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.11/apache-rat-project-0.11.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.6/apache-rat-project-0.6.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.10/apache-rat-tasks-0.10.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.11/apache-rat-tasks-0.11.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-tasks/0.6/apache-rat-tasks-0.6.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10/apache-rat-0.10.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.10/apache-rat-0.10.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11/apache-rat-0.11.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat/0.11/apache-rat-0.11.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-apache-rat/LICENSE
/usr/share/package-licenses/mvn-apache-rat/NOTICE
/usr/share/package-licenses/mvn-apache-rat/apache-rat-core_src_test_resources_elements_LICENSE
/usr/share/package-licenses/mvn-apache-rat/apache-rat-core_src_test_resources_elements_NOTICE
