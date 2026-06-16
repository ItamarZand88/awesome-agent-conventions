<!-- source: fame2 — https://raw.githubusercontent.com/HimangshuPronoy/fame2/main/.kiro/steering/structure.md -->
# Project Structure

## Directory Organization

```
src/
├── app/                    # Next.js App Router pages
│   ├── page.tsx           # Homepage
│   ├── layout.tsx         # Root layout with AuthProvider
│   ├── globals.css        # Global styles
│   ├── login/             # Authentication page
│   ├── dashboard/         # User dashboard
│   │   ├── admin/         # Admin-only dashboard
│   │   └── user/          # User-specific dashboard
│   ├── listings/          # Browse all listings
│   ├── listing/[id]/      # Individual listing detail page
│   ├── concierge/         # Concierge service page
│   ├── journal/           # User journal page
│   └── partners/          # Partner portal page
├── components/            # Reusable React components
│   ├── Header.tsx         # Main navigation header
│   ├── Footer.tsx         # Site footer
│   ├── ListingGrid.tsx    # Listing display grid
│   ├── SearchBar.tsx      # Search functionality
│   └── *.module.css       # Component-scoped styles
└── lib/                   # Shared utilities and configs
    ├── supabase.ts        # Supabase client setup + types
    └── auth-context.tsx   # Authentication context provider

supabase/
└── schema.sql             # Database schema and seed data
```

## Architectural Patterns

### Routing
- File-based routing via Next.js App Router
- Dynamic routes use `[param]` syntax (e.g., `listing/[id]`)
- Route groups for related pages (e.g., `dashboard/admin`, `dashboard/user`)

### Component Structure
- Each component has a paired `.module.css` file
- Client components marked with `"use client"` directive
- Server components by default (no directive needed)

### Data Fetching
- Client-side: Use `supabase` client with `useEffect` hooks
- Server-side: Use `supabase` client in Server Components or Server Actions
- Admin operations: Use `supabaseAdmin` (only in server context)

### Authentication
- `AuthProvider` wraps the app in `src/app/layout.tsx`
- `useAuth()` hook provides user, profile, session, and auth methods
- Role-based access via `isAdmin` flag

### Styling Conventions
- CSS Modules with camelCase class names
- Consistent naming: `component.module.css` for `Component.tsx`
- Import as: `import styles from "./Component.module.css"`
- Use: `className={styles.className}`

### Type Safety
- Database types defined in `src/lib/supabase.ts`
- Export interfaces: `Profile`, `Listing`
- Use these types throughout the application
