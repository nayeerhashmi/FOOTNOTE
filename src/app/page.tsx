import { siteConfig } from "@/lib/site";

export default function HomePage() {
  return (
    <main className="foundation-shell">
      <div className="foundation-topline">
        <span>{siteConfig.name}</span>
        <span>Independent culture magazine</span>
      </div>

      <section className="foundation-message" aria-labelledby="foundation-title">
        <p className="foundation-kicker">Jammu and Kashmir · Est. 2026</p>
        <h1 id="foundation-title">A publication is taking shape.</h1>
        <p className="foundation-copy">
          The digital foundation for FOOTNOTE is in place. The magazine cover,
          book reader and editorial sections will be built in the next stages.
        </p>
        <p className="foundation-status">Website foundation · Milestone 1</p>
      </section>

      <footer className="foundation-footer">
        <span>Stories. Sound. Memory.</span>
        <span>FOOTNOTE</span>
      </footer>
    </main>
  );
}
