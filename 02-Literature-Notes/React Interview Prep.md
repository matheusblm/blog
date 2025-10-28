### Composition vs inheritance

Composition its one of the ways to avoid the props drilling, because you compose components by nesting example:

```
function Card({ children }) {
  return <div className="card">{children}</div>;
}

function Profile() {
  return (
    <Card>
      <img src="avatar.png" />
      <h2>Matheus</h2>
    </Card>
  );
}
```

### Zustand (or Context Api) Global State Management

Its more simple and easy to create, don't need a provider


```
import { create } from "zustand";
const useStore = create(set => ({
  count: 0,
  increment: () => set(state => ({ count: state.count + 1 })),
}));

function Counter() {
  const { count, increment } = useStore();
  return <button onClick={increment}>{count}</button>;
}
```


### useMemo vs useCallback vs React.memo

| Hook / Function | What it Memoizes                      | When to Use                                                                                                                                                                                                                    | Example                                                    |
| --------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **useMemo**     | The **result/value** of a computation | Heavy computations or                                                                                                                                                                                                          | `const sorted = useMemo(() => sort(arr), [arr])`           |
| useCallbak      | The function referenc When passing functions to child components to avoid re-render, every time the values on the function change the function react will create a new function, so if the values doesn't change will remain the same function ge  ge  ge  ge  ge  ge  | `const handleClick = useCallback(() => setCount(c+1), [])` |
| React.memo      | The **component render output**       | Prevent re-rende                                                                                                                                                                                                               | `export default React.memo(MyComponent)`                   |
### Code Splitting & Lazy Loading

Only load parts of the app when needed


```
import React, { lazy, Suspense } from "react";

const Settings = lazy(() => import("./Settings"));

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Settings />
    </Suspense>
  );
}
```


### Virtualization (React Window)

Render large list of data quickly, because only visible items

```
import { FixedSizeList as List } from "react-window";

<List
  height={400}
  itemCount={10000}
  itemSize={35}
  width={300}
>
  {({ index, style }) => <div style={style}>Item {index}</div>}
</List>
```

## Next.JS

| Type                                      | Runs Where        | When to Use                                          | Example                              |
| ----------------------------------------- | ----------------- | ---------------------------------------------------- | ------------------------------------ |
| **CSR (Client-Side Rendering)**           | Browser           | Dynamic UI that depends on user input or local state | React SPA                            |
| **SSR (Server-Side Rendering)**           | Server            | Fresh data on every request (auth, dashboards)       | `getServerSideProps`                 |
| **SSG (Static Site Generation)**          | Build time        | Content that rarely changes                          | `getStaticProps`                     |
| **ISR (Incremental Static Regeneration)** | Build + On-demand | Semi-dynamic pages; revalidate periodically          | `getStaticProps({ revalidate: 60 })` |

### Normalization

Organizar os dados para evitar redundancias e manter a integridade dos dados

| Form                                     | Goal                                       | Example Fix                                                                     |
| ---------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| **1NF – No repeating groups**            | Each cell has one value only               | Split a “phones = 123,456” column into multiple rows                            |
| **2NF – Remove partial dependencies**    | Non-key fields must depend on the full key | If composite key `(StudentID, CourseID)` → move `StudentName` to its own table  |
| **3NF – Remove transitive dependencies** | Non-key fields depend only on the key      | If `EmployeeID → Department → Location`, move `Location` to `Departments` table |


| Name        | Item              | Address              | Newsletter           | Supplier  | Supplier Phone  | Price |
| ----------- | ----------------- | -------------------- | -------------------- | --------- | --------------- | ----- |
| Alan Smith  | Xbox One          | 35 Pal ST, Miamai    | Xbox News            | Microsoft | (800) BUY-XBOX  | 250   |
| Roger Banks | Play 4            | 47 Campus, Rd Boston | Play News            | Sony      | (800) BUY-SONY  | 300   |
| Evan Wilson | Xbox One, Ps Vite | 28 Rock Av, Denver   | Xbox News, Play News | Wholesale | Toll Free       | 450   |
| Alan Smith  | Play 4            | 47 Campus Rd, Boston | Play News            | Sony      | (800) BUY-sSONY | 300   |

1ST Normal Form 
- Each Cell to be Single Valued
- Entries in a column are same type
- Rows uniquely Identified - Add Unique ID, or add more columns to make unique

After the 1st Normal

| Name        | Item     | Address              | Newsletter           | Supplier  | Supplier Phone  | Price | Cust ID  |
| ----------- | -------- | -------------------- | -------------------- | --------- | --------------- | ----- | -------- |
| Alan Smith  | Xbox One | 35 Pal ST, Miamai    | Xbox News            | Microsoft | (800) BUY-XBOX  | 250   | at_smith |
| Roger Banks | Play 4   | 47 Campus, Rd Boston | Play News            | Sony      | (800) BUY-SONY  | 300   | roger25  |
| Evan Wilson | Xbox One | 28 Rock Av, Denver   | Xbox News, Play News | Microsofy | (800) BUY-XBOX  | 250   | wilson44 |
| Evan Wilson | Ps Vita  | 28 Rock Av, Denver   | Xbox News, Play News | Sony      | (800)  BUY-SONY | 200   | wilson44 |
| Alan Smith  | Play 4   | 47 Campus Rd, Boston | Play News            | Sony      | (800) BUY-sSONY | 300   | 300      |

2nd Normal Form
- All attributes (Non-key Columns) dependent on the key
- If the column don't be the same "family" like the key column, need to be on other table

| Name        | Address              | Newsletter           | Cust ID  |
| ----------- | -------------------- | -------------------- | -------- |
| Alan Smith  | 35 Pal ST, Miamai    | Xbox News            | at_smith |
| Roger Banks | 47 Campus, Rd Boston | Play News            | roger25  |
| Evan Wilson | 28 Rock Av, Denver   | Xbox News, Play News | wilson44 |
| Evan Wilson | 28 Rock Av, Denver   | Xbox News, Play News | wilson44 |
| Alan Smith  | 47 Campus Rd, Boston | Play News            | am_smith |

| Item     | Supplier  | Supplier Phone  | Price |
| -------- | --------- | --------------- | ----- |
| Xbox One | Microsoft | (800) BUY-XBOX  | 250   |
| Play 4   | Sony      | (800) BUY-SONY  | 300   |
| Ps Vita  | Sony      | (800)  BUY-SONY | 200   |


| Cust Id  | Item     |
| -------- | -------- |
| at_smith | Xbox One |
| roger25  | Play 4   |
| wilson44 | Xbox One |
| wilson44 | Ps Vita  |
| am_smith | Play 4   |

3rd Normal Form - All fields (columns) can be determined only by the key in the table and no other column

| Item     | Supplier  | Price |
| -------- | --------- | ----- |
| Xbox One | Microsoft | 250   |
| Play 4   | Sony      | 300   |
| Ps Vita  | Sony      | 200   |

| Supplier  | Supplier Phone  |
| --------- | --------------- |
| Microsoft | (800) BUY-XBOX  |
| Sony      | (800) BUY-SONY  |

4th normal form - No multi-valued dependencies


| Name        | Address              | Cust ID  |
| ----------- | -------------------- | -------- |
| Alan Smith  | 35 Pal ST, Miamai    | at_smith |
| Roger Banks | 47 Campus, Rd Boston | roger25  |
| Evan Wilson | 28 Rock Av, Denver   | wilson44 |
| Alan Smith  | 47 Campus Rd, Boston | am_smith |

| Newsletter           | Cust ID  |
| -------------------- | -------- |
| Xbox News            | at_smith |
| Play News            | roger25  |
| Xbox News, Play News | wilson44 |
| Xbox News, Play News | wilson44 |
| Play News            | am_smith |


The result is cleaner tables with predictable relationships


### Left Join, Right Join, Inner Join

All three are used to combine rows from two tables.


| Join Type  | Keeps All From    | Shows Unmatched As NULL | Common Use                                     |
| ---------- | ----------------- | ----------------------- | ---------------------------------------------- |
| INNER JOIN | Only matched rows | None                    | When you need data from both tables that match |
| LEFT JOIN  | Left table        | Right side              | Show all left items even if missing matches    |
| RIGHT JOIN | Right table       | Left side               | Show all right items even if missing matches   |
