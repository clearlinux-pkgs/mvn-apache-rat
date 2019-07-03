#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-apache-rat
Version  : 0.11
Release  : 2
URL      : https://github.com/apache/creadur-rat/archive/apache-rat-project-0.11.tar.gz
Source0  : https://github.com/apache/creadur-rat/archive/apache-rat-project-0.11.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar
Source2  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom
Source3  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar
Source4  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom
Source5  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar
Source6  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom
Source7  : https://repo1.maven.org/maven2/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-apache-rat-data = %{version}-%{release}

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


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom
/usr/share/java/.m2/repository/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom
