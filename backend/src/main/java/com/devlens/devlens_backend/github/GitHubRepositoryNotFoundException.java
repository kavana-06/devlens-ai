package com.devlens.devlens_backend.github;

public class GitHubRepositoryNotFoundException extends RuntimeException {

    public GitHubRepositoryNotFoundException(String owner, String repositoryName) {
        super("GitHub repository '" + owner + "/" + repositoryName + "' not found");
    }
}
