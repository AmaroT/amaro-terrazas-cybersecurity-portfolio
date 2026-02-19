# Secure JWT Authentication Example (Java/Spring Boot)

From CS-305 coursework: Implementing basic auth with JWT to prevent common web vulns.

**Key Secure Practices:**
- Use strong secret key
- HS256 algorithm
- Validate expiration/issuer
- Input sanitization

**Code Snippet:**
```java
// SecurityConfig.java excerpt
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.csrf().disable()
        .authorizeRequests()
        .antMatchers("/api/public/**").permitAll()
        .anyRequest().authenticated()
        .and()
        .addFilter(new JwtAuthenticationFilter(authenticationManager()));
    return http.build();
}

// JwtUtil.java - Token generation/validation
public String generateToken(UserDetails userDetails) {
    return Jwts.builder()
        .setSubject(userDetails.getUsername())
        .setIssuedAt(new Date())
        .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60 * 10)) // 10h
        .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
        .compact();
}