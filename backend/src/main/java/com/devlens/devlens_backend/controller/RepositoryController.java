package com.devlens.devlens_backend.controller;

import com.devlens.devlens_backend.repository.Repository;
import com.devlens.devlens_backend.repository.RepositoryService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/repositories")
public class RepositoryController {

    private final RepositoryService repositoryService;

    public RepositoryController(RepositoryService repositoryService) {
        this.repositoryService = repositoryService;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Repository createRepository(
            @Valid @RequestBody Repository repository) {

        return repositoryService.createRepository(repository);
    }

    @GetMapping
    public List<Repository> getAllRepositories() {
        return repositoryService.getAllRepositories();
    }

    @GetMapping("/{id}")
    public Repository getRepositoryById(@PathVariable Long id) {
        return repositoryService.getRepositoryById(id);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteRepository(@PathVariable Long id) {
        repositoryService.deleteRepository(id);
    }
}