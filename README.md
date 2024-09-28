# Blooprint-Inventory
This project is a RESTful API for managing inventory items. The API is built using Django Rest Framework (DRF) with PostgreSQL as the database. It uses Redis for caching frequently accessed items, JWT for authentication, and integrates a logging system for debugging and monitoring. Unit tests are implemented using Django's test framework.

<h3>Installation</h3>
<ul>
  <li>Python3</li>
  <li>PostgreSQL</li>
  <li>Redis</li>
  <li>Django and Django Rest Framework</li>
  <li>pip</li>
</ul>

<h2>Steps</h2>
<ol>
  <li>Clone the repository</li>
  <li>Install the required Python packages</li>
  <li>Set up PostgreSQL and configure the database in <code>settings.py</code>.</li>
  <li>Set up Redis and configure it in <code>settings.py</code>.</li>
  <li>Run database migrations:
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li>Run the development server:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>Run unit tests:
    <pre><code>python manage.py test</code></pre>
  </li>
</ol>
