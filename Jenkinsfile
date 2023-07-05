@Library('jenkins-shared-library-turing')_
def GIT_URL = "https://github.com/TuringEnterprises/magic-lens.git"
def GIT_CREDENTIAL_ID = "a3445fa2-3736-4c7b-bdb8-7ffd7fedf257"
def GIT_SHA
def BRANCH = env.BRANCH_NAME

pipeline {
    agent {
        label "jenkins-build-only"
    }
    environment {
        GOOGLE_PROJECT_ID="turing-230020"
        GOOGLE_SERVICE_ACCOUNT_KEY=credentials('google_service_account_key');
        TURING_GITMACHINE_TOKEN=credentials('turing-gitmachin-token');
    }
    stages {
        stage("Check out") {
            when {
                anyOf {
                    branch 'develop'
                    branch 'staging'
                    branch 'main'
                }
            }
            steps {
                script {
                    // Trigger not from PR
                    def scmVars = checkout([$class: 'GitSCM',
                        branches: [[name: env.BRANCH_NAME]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'SubmoduleOption',
                                disableSubmodules: false,
                                parentCredentials: true,
                                recursiveSubmodules: true,
                                reference: '',
                                trackingSubmodules: false
                            ]
                        ],
                        submoduleCfg: [],
                        userRemoteConfigs: [[credentialsId: "a3445fa2-3736-4c7b-bdb8-7ffd7fedf257", url: "git@github.com:TuringEnterprises/magic-lens.git"]]
                    ])
                }
            }
        }

        stage("build imager") {
            when {
                anyOf {
                    branch 'develop'
                    branch 'staging'
                    branch 'main'
                }
            }
            steps {
                script {
                    deployQuirv.build("backend", BRANCH)
                }
            }
        }
        stage("Deploy backend") {
            when {
                anyOf {
                    branch 'develop'
                    branch 'staging'
                    branch 'main'
                }
            }
            steps {
                script {
                    deployQuirv.applyHelmToKube("magic-lens","backend", BRANCH, BUILD_NUMBER)
                    deployQuirv.applyHelmToKube("magic-lens","frontend", BRANCH, BUILD_NUMBER)
                }
            }
        }
    }
}
