package com.devlens.devlens_backend.repository;

import com.devlens.devlens_backend.exception.RepositoryNotFoundException;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RepositoryService {

    private final RepositoryRepository repositoryRepository;

    public RepositoryService(RepositoryRepository repositoryRepository) {
        this.repositoryRepository = repositoryRepository;
    }

    public Repository createRepository(Repository repository) {
        return repositoryRepository.save(repository);
    }

    public List<Repository> getAllRepositories() {
        return repositoryRepository.findAll();
    }

    public Repository getRepositoryById(Long id) {
        return repositoryRepository.findById(id)
                .orElseThrow(() -> new RepositoryNotFoundException(id));
    }

    public void deleteRepository(Long id) {
        if (!repositoryRepository.existsById(id)) {
            throw new RepositoryNotFoundException(id);
        }

        repositoryRepository.deleteById(id);
    }
}