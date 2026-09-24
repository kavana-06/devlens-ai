package com.devlens.devlens_backend.github;

import com.fasterxml.jackson.annotation.JsonProperty;

public class GitHubRepositoryResponse {

    private final Long id;
    private final String name;
    private final String fullName;
    private final String owner;
    private final String htmlUrl;
    private final String description;
    private final String defaultBranch;

    @JsonProperty("private")
    private final boolean privateRepository;

    private final int stars;
    private final int forks;
    private final int openIssues;

    public GitHubRepositoryResponse(
            Long id,
            String name,
            String fullName,
            String owner,
            String htmlUrl,
            String description,
            String defaultBranch,
            boolean privateRepository,
            int stars,
            int forks,
            int openIssues) {

        this.id = id;
        this.name = name;
        this.fullName = fullName;
        this.owner = owner;
        this.htmlUrl = htmlUrl;
        this.description = description;
        this.defaultBranch = defaultBranch;
        this.privateRepository = privateRepository;
        this.stars = stars;
        this.forks = forks;
        this.openIssues = openIssues;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getFullName() {
        return fullName;
    }

    public String getOwner() {
        return owner;
    }

    public String getHtmlUrl() {
        return htmlUrl;
    }

    public String getDescription() {
        return description;
    }

    public String getDefaultBranch() {
        return defaultBranch;
    }

    public boolean isPrivate() {
        return privateRepository;
    }

    public int getStars() {
        return stars;
    }

    public int getForks() {
        return forks;
    }

    public int getOpenIssues() {
        return openIssues;
    }
}