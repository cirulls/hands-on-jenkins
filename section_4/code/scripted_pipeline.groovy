#!/usr/bin/groovy
// Scripted Pipeline
node {

	stage('Build') {
		echo 'Building....'
	}

	stage('Test') {
		echo 'Building....'
	}

	stage('Deploy') {
		echo 'Deploying....'
	}
}
