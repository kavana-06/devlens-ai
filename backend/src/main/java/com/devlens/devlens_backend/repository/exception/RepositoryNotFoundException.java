package com.devlens.devlens_backend.exception;

public class RepositoryNotFoundException extends RuntimeException {

    public RepositoryNotFoundException(Long id) {
        super("Repository with id " + id + " not found");
    }
}