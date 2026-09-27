export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      {/* Navigation */}
      <nav className="border-b border-slate-800">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">
          <div className="flex items-center gap-3">
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-blue-600 font-bold">
              D
            </div>

            <span className="text-xl font-semibold">
              DevLens
            </span>
          </div>

          <div className="hidden items-center gap-8 text-sm text-slate-300 md:flex">
            <a
              href="#features"
              className="transition hover:text-white"
            >
              Features
            </a>

            <a
              href="#how-it-works"
              className="transition hover:text-white"
            >
              How it works
            </a>

            <a
              href="#technology"
              className="transition hover:text-white"
            >
              Technology
            </a>
          </div>

          <button className="rounded-lg bg-blue-600 px-5 py-2.5 text-sm font-medium transition hover:bg-blue-500">
            Analyze Repository
          </button>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(37,99,235,0.18),transparent_45%)]" />

        <div className="relative mx-auto max-w-7xl px-6 py-24 md:py-32">
          <div className="max-w-4xl">
            <div className="mb-6 inline-flex items-center rounded-full border border-blue-500/30 bg-blue-500/10 px-4 py-2 text-sm text-blue-300">
              AI Software Change Intelligence
            </div>

            <h1 className="text-5xl font-bold leading-tight tracking-tight md:text-7xl">
              Understand your codebase
              <span className="text-blue-500"> before </span>
              you change it.
            </h1>

            <p className="mt-8 max-w-3xl text-lg leading-8 text-slate-400 md:text-xl">
              DevLens analyzes your repository, maps dependencies,
              understands architecture, and predicts what could be
              affected by a code change.
            </p>

            <div className="mt-10 flex flex-col gap-4 sm:flex-row">
              <button className="rounded-lg bg-blue-600 px-7 py-3.5 font-semibold transition hover:bg-blue-500">
                Analyze a Repository
              </button>

              <button className="rounded-lg border border-slate-700 bg-slate-900 px-7 py-3.5 font-semibold transition hover:border-slate-600 hover:bg-slate-800">
                Explore DevLens
              </button>
            </div>
          </div>

          {/* Product preview */}
          <div className="mt-20 rounded-2xl border border-slate-800 bg-slate-900/80 p-5 shadow-2xl">
            <div className="rounded-xl border border-slate-800 bg-slate-950">
              <div className="flex items-center gap-2 border-b border-slate-800 px-5 py-4">
                <div className="h-3 w-3 rounded-full bg-red-500" />
                <div className="h-3 w-3 rounded-full bg-yellow-500" />
                <div className="h-3 w-3 rounded-full bg-green-500" />

                <span className="ml-4 text-sm text-slate-500">
                  DevLens Analysis
                </span>
              </div>

              <div className="grid gap-6 p-6 md:grid-cols-3">
                <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
                  <p className="text-sm text-slate-500">
                    Repository
                  </p>

                  <p className="mt-2 font-semibold">
                    my-project
                  </p>

                  <p className="mt-3 text-sm text-green-400">
                    Analysis complete
                  </p>
                </div>

                <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
                  <p className="text-sm text-slate-500">
                    Dependencies
                  </p>

                  <p className="mt-2 text-3xl font-bold">
                    127
                  </p>

                  <p className="mt-2 text-sm text-slate-400">
                    relationships detected
                  </p>
                </div>

                <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
                  <p className="text-sm text-slate-500">
                    Potential impact
                  </p>

                  <p className="mt-2 text-3xl font-bold text-yellow-400">
                    8 files
                  </p>

                  <p className="mt-2 text-sm text-slate-400">
                    may be affected
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section
        id="features"
        className="border-t border-slate-800 bg-slate-900/40"
      >
        <div className="mx-auto max-w-7xl px-6 py-24">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-wider text-blue-400">
              What DevLens does
            </p>

            <h2 className="mt-4 text-4xl font-bold">
              Your codebase, understood as a system.
            </h2>

            <p className="mt-5 text-lg leading-8 text-slate-400">
              DevLens combines code analysis, dependency intelligence,
              Git history, and AI reasoning to help developers understand
              the consequences of software changes.
            </p>
          </div>

          <div className="mt-14 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            <FeatureCard
              title="Change Impact Analysis"
              description="Find the components, files, services, and tests that could be affected before you modify code."
            />

            <FeatureCard
              title="Architecture Intelligence"
              description="Understand how the major parts of a repository connect and communicate."
            />

            <FeatureCard
              title="Dependency Graph"
              description="Build a living map of relationships between modules and components."
            />

            <FeatureCard
              title="AI Repository Assistant"
              description="Ask questions about your repository and receive answers grounded in repository evidence."
            />

            <FeatureCard
              title="Pull Request Intelligence"
              description="Analyze a Git diff and identify potential impact, risks, and missing tests."
            />

            <FeatureCard
              title="Security Analysis"
              description="Combine static analysis and AI reasoning to identify security-sensitive areas."
            />
          </div>
        </div>
      </section>

      {/* How it works */}
      <section id="how-it-works">
        <div className="mx-auto max-w-7xl px-6 py-24">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-wider text-blue-400">
              How it works
            </p>

            <h2 className="mt-4 text-4xl font-bold">
              From repository to software intelligence.
            </h2>
          </div>

          <div className="mt-14 grid gap-8 md:grid-cols-4">
            <Step
              number="01"
              title="Connect"
              description="Connect a GitHub repository to DevLens."
            />

            <Step
              number="02"
              title="Analyze"
              description="Parse source code, Git history, and repository structure."
            />

            <Step
              number="03"
              title="Understand"
              description="Build dependency and architectural relationships."
            />

            <Step
              number="04"
              title="Predict"
              description="Use the software model to explain potential change impact."
            />
          </div>
        </div>
      </section>

      {/* Technology */}
      <section
        id="technology"
        className="border-t border-slate-800 bg-slate-900/40"
      >
        <div className="mx-auto max-w-7xl px-6 py-24">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-wider text-blue-400">
              Engineering
            </p>

            <h2 className="mt-4 text-4xl font-bold">
              Built as an engineering system, not a chatbot wrapper.
            </h2>

            <p className="mt-5 text-lg leading-8 text-slate-400">
              DevLens combines multiple technologies so the AI has real
              software-engineering context to reason over.
            </p>
          </div>

          <div className="mt-12 flex flex-wrap gap-3">
            {[
              "Next.js",
              "React",
              "TypeScript",
              "Java",
              "Spring Boot",
              "Python",
              "FastAPI",
              "PostgreSQL",
              "Git",
              "AST Analysis",
              "Dependency Graphs",
              "RAG",
              "LLM",
              "Docker",
            ].map((technology) => (
              <span
                key={technology}
                className="rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-sm text-slate-300"
              >
                {technology}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800">
        <div className="mx-auto flex max-w-7xl flex-col gap-3 px-6 py-8 text-sm text-slate-500 md:flex-row md:items-center md:justify-between">
          <p>DevLens AI</p>

          <p>
            AI Software Change Intelligence Platform
          </p>
        </div>
      </footer>
    </main>
  );
}

function FeatureCard({
  title,
  description,
}: {
  title: string;
  description: string;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950 p-6 transition hover:border-slate-700">
      <h3 className="text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-3 leading-7 text-slate-400">
        {description}
      </p>
    </div>
  );
}

function Step({
  number,
  title,
  description,
}: {
  number: string;
  title: string;
  description: string;
}) {
  return (
    <div>
      <p className="text-sm font-semibold text-blue-400">
        {number}
      </p>

      <h3 className="mt-3 text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-3 leading-7 text-slate-400">
        {description}
      </p>
    </div>
  );
}