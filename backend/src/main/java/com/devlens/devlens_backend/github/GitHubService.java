package com.devlens.devlens_backend.github;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.util.Map;

@Service
public class GitHubService {

    private final RestClient restClient;

    public GitHubService() {
        this.restClient = RestClient.builder()
                .baseUrl("https://api.github.com")
                .build();
    }

    public GitHubRepositoryResponse getRepository(
            String owner,
            String repositoryName) {

        Map<String, Object> repository = restClient
                .get()
                .uri("/repos/{owner}/{repositoryName}", owner, repositoryName)
                .retrieve()
                .body(Map.class);

        if (repository == null) {
            throw new IllegalStateException(
                    "GitHub returned an empty repository response"
            );
        }

        Map<String, Object> githubOwner =
                (Map<String, Object>) repository.get("owner");

        String ownerLogin =
                githubOwner != null
                        ? (String) githubOwner.get("login")
                        : null;

        return new GitHubRepositoryResponse(
                ((Number) repository.get("id")).longValue(),
                (String) repository.get("name"),
                (String) repository.get("full_name"),
                ownerLogin,
                (String) repository.get("html_url"),
                (String) repository.get("description"),
                (String) repository.get("default_branch"),
                (Boolean) repository.get("private"),
                ((Number) repository.get("stargazers_count")).intValue(),
                ((Number) repository.get("forks_count")).intValue(),
                ((Number) repository.get("open_issues_count")).intValue()
        );
    }
}