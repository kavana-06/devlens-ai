package com.devlens.devlens_backend.github;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class GitHubServiceTest {

    @Test
    void shouldFetchGitHubRepository() {
        GitHubService gitHubService = new GitHubService();

        GitHubRepositoryResponse response =
                gitHubService.getRepository("kavana-06", "devlens-ai");

        assertNotNull(response);
        assertEquals("devlens-ai", response.getName());
        assertEquals("kavana-06/devlens-ai", response.getFullName());
        assertEquals("kavana-06", response.getOwner());
        assertEquals("main", response.getDefaultBranch());
        assertFalse(response.isPrivate());
    }
}