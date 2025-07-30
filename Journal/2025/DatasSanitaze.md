Dont Try to sanitize input. Escape outpu.

Sanitizing user input to prevent cross-site scripting attacks.

How does cross-site scripiting happen?

If user can enter information that the site repeats back to them verbatim in a page's html.

Why input filtering isnt a great idea

Maybe you write some code to strip out unsafe HTML characters <>&, you receive a a false sense of security, because you are still open a css, json, sql even shell scripts attacks.

If an attacker sets their name to include double quotes, like "; badFunc(); "


the same for a SQL injection 

ex: $query = "SELECT * FROM users WHERE name = '{$name}'"

** ESCAPE YOUR OUTPUT INSTEAD **

$stmt = $db->prepare('SELECT * FROM users WHERE name = ?');
$stmt->bind_param('s', $name);

Save the user enters verbatim

** But what if you want raw input? **

Allow them to only enter pure Markdown, and convert that to HTML on render (many Markdown libraries allow raw HTML by default; be sure to disable that). This is the most secure option, but also more restrictive.
Allow them to use HTML in the Markdown, but only a whitelist of allowed tags and attributes, such as <a href="..."> and <img src="...">. Both Stack Exchange and GitHub take this second approach.

