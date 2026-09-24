package com.devlens.devlens_backend.repository;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

@Entity
@Table(name = "repositories")
public class Repository {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Repository name is required")
    @Column(nullable = false)
    private String name;

    @NotBlank(message = "Repository owner is required")
    @Column(nullable = false)
    private String owner;

    @NotBlank(message = "GitHub URL is required")
    @Pattern(
            regexp = "^https://github\\.com/[^/]+/[^/]+/?$",
            message = "GitHub URL must be a valid GitHub repository URL"
    )
    @Column(nullable = false)
    private String githubUrl;

    public Repository() {
    }

    public Repository(String name, String owner, String githubUrl) {
        this.name = name;
        this.owner = owner;
        this.githubUrl = githubUrl;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getOwner() {
        return owner;
    }

    public String getGithubUrl() {
        return githubUrl;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public void setGithubUrl(String githubUrl) {
        this.githubUrl = githubUrl;
    }
}