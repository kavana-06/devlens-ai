package com.devlens.devlens_backend.github;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/github")
public class GitHubController {

    private final GitHubService gitHubService;

    public GitHubController(GitHubService gitHubService) {
        this.gitHubService = gitHubService;
    }

    @GetMapping("/repositories/{owner}/{repositoryName}")
    public GitHubRepositoryResponse getRepository(
            @PathVariable String owner,
            @PathVariable String repositoryName) {

        return gitHubService.getRepository(owner, repositoryName);
    }
}