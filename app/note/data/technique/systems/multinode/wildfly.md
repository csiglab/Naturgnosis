# Wildfly

## Formulation

### What technical element type does this technical instance belong to?

**WildFly belongs to the `Production Technical System` technical element type.**

More specifically:

```text
Production Technical System
└── WildFly
```

WildFly is a technical system because it is an organized composition of software runtime components, services, subsystems, interfaces, configuration, dependencies, and management mechanisms that collectively provide an application-server runtime.

### What is this technical instance?

> WildFly is a concrete modular application-server technical system instance providing a managed runtime for deploying, executing, integrating, securing, and managing enterprise applications and supporting technical services.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one WildFly server distribution instance (artefacts, configuration surface, runtime structure, practices); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete file, process, configuration attribute, measured value, or named actor; attribute slots (Port, Version, Name) are terminal by rule.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Constitutive techniques in this table are those the WildFly system embodies in constituting its objects, not the programmers' external build toolchain.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → WildFly | Running WildFly application-server platform instance. |
| `Production Technical System` → WildFly → Distribution | Installed WildFly server distribution from which the runtime is provisioned. |
| `Production Technical System` → WildFly → Distribution → WildFly Home | Root filesystem location containing the server installation. |
| `Production Technical System` → WildFly → Distribution → `bin/` | Executable scripts and command-line entry points. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.sh` | Standalone server launch script. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.bat` | Windows standalone server launch script. |
| `Production Technical System` → WildFly → Distribution → Standalone Launch | Situated launching of a standalone server process by an operator. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.sh` | Managed-domain launch script. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.bat` | Windows managed-domain launch script. |
| `Production Technical System` → WildFly → Distribution → Domain Launch | Situated launching of managed-domain processes by an operator. |
| `Production Technical System` → WildFly → Distribution → `bin/jboss-cli.sh` | Management CLI launcher script. |
| `Production Technical System` → WildFly → Distribution → `bin/jboss-cli.bat` | Windows management CLI launcher script. |
| `Production Technical System` → WildFly → Distribution → `bin/add-user.sh` | User and identity configuration script. |
| `Production Technical System` → WildFly → Distribution → `bin/add-user.bat` | Windows user and identity configuration script. |
| `Production Technical System` → WildFly → Distribution → `bin/elytron-tool.sh` | Elytron security utility script. |
| `Production Technical System` → WildFly → Distribution → `bin/elytron-tool.bat` | Windows Elytron security utility script. |
| `Production Technical System` → WildFly → Distribution → `bin/client/` | Client library directory for remote access. |
| `Production Technical System` → WildFly → Distribution → `bin/client/jboss-cli-client.jar` | Client library for remote management access. |
| `Production Technical System` → WildFly → Distribution → `bin/init.d/` | Unix service initialization scripts. |
| `Production Technical System` → WildFly → Distribution → `bin/service/` | Service wrapper definitions. |
| `Production Technical System` → WildFly → Distribution → `bin/jboss-cli.xml` | CLI configuration file. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.conf` | Standalone JVM launch configuration (heap, system properties). |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.conf.bat` | Windows standalone JVM launch configuration. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.conf` | Domain-mode JVM launch configuration. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.conf.bat` | Windows domain-mode JVM launch configuration. |
| `Production Technical System` → WildFly → Distribution → `modules` | JBoss Modules repository containing server modules. |
| `Production Technical System` → WildFly → Distribution → `modules → Module` | Isolated module containing classes/resources and dependency metadata. |
| `Production Technical System` → WildFly → Distribution → `modules → Module → module.xml` | Module dependency and resource declaration. |
| `Production Technical System` → WildFly → Distribution → `modules/system/layers/base/` | Base layer containing core WildFly modules. |
| `Production Technical System` → WildFly → Distribution → `standalone/` | Standalone-server runtime state and configuration tree. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/` | Standalone server configuration repository. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` | Main standalone server configuration (default profile). |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-full.xml` | Full standalone configuration profile including additional services such as messaging. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-ha.xml` | Standalone high-availability configuration profile. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-full-ha.xml` | Full high-availability standalone configuration. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-microprofile.xml` | MicroProfile standalone configuration profile. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-microprofile-ha.xml` | MicroProfile high-availability configuration profile. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone-load-balancer.xml` | Load-balancer configuration profile. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/mgmt-users.properties` | Management user credentials store. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/mgmt-groups.properties` | Management group-to-role mapping. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/application-users.properties` | Application user credentials store. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/application-roles.properties` | Application user-to-role mapping. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/logging.properties` | Logging configuration properties. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone_xml_history/` | Configuration change history. |
| `Production Technical System` → WildFly → Distribution → `standalone/deployments/` | Deployment content and deployment markers. |
| `Production Technical System` → WildFly → Distribution → `standalone/data/` | Runtime-generated persistent server data. |
| `Production Technical System` → WildFly → Distribution → `standalone/data/content/` | Content repository for deployed artifacts. |
| `Production Technical System` → WildFly → Distribution → `standalone/data/timer-service-data/` | EJB timer persistence data. |
| `Production Technical System` → WildFly → Distribution → `standalone/data/tx-object-store/` | Transaction object store. |
| `Production Technical System` → WildFly → Distribution → `standalone/log/` | Runtime log storage. |
| `Production Technical System` → WildFly → Distribution → `standalone/log/server.log` | Main server log file. |
| `Production Technical System` → WildFly → Distribution → `standalone/log/audit.log` | Management audit log. |
| `Production Technical System` → WildFly → Distribution → `standalone/tmp/` | Runtime temporary data. |
| `Production Technical System` → WildFly → Distribution → `standalone/tmp/vfs/` | Virtual file system cache for deployments. |
| `Production Technical System` → WildFly → Distribution → `docs/` | Documentation and schema files. |
| `Production Technical System` → WildFly → Distribution → `docs/schema/` | XML schema definitions for configuration files. |
| `Production Technical System` → WildFly → Domain Distribution | Domain-mode configuration and process-management structure. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` | Domain-wide profiles, server groups and subsystem configuration. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` | Host Controller configuration. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host-master.xml` | Master Host Controller configuration. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host-slave.xml` | Slave Host Controller configuration. |
| `Production Technical System` → WildFly → Domain Distribution → Host Controller | Process responsible for managing server processes on a host. |
| `Production Technical System` → WildFly → Domain Distribution → Configuration Propagation Flow | Host controller propagating configuration to managed servers. |
| `Production Technical System` → WildFly → Domain Distribution → Domain Controller | Process responsible for managing the domain-wide configuration. |
| `Production Technical System` → WildFly → Domain Distribution → Deployment Distribution Flow | Domain controller distributing deployments to server groups. |
| `Production Technical System` → WildFly → Domain Distribution → Server Group | Named collection of server instances sharing a profile and socket binding group. |
| `Production Technical System` → WildFly → Domain Distribution → Profile | Named configuration profile containing subsystem configurations. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/servers/` | Runtime state of managed servers. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/data/` | Domain persistent runtime data. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/log/` | Domain log storage. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/tmp/` | Domain temporary data. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/deployments/` | Domain deployment content. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain_xml_history/` | Domain configuration change history. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host_xml_history/` | Host configuration change history. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/application-users.properties` | Application user credentials store. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/application-roles.properties` | Application user-to-role mapping. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/mgmt-users.properties` | Management user credentials store. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/mgmt-groups.properties` | Management group-to-role mapping. |
| `Production Technical System` → WildFly → Runtime | Executing WildFly server runtime. |
| `Production Technical System` → WildFly → Runtime → JVM | Java Virtual Machine executing WildFly. |
| `Production Technical System` → WildFly → Runtime → Java Process | Operating-system process containing the WildFly runtime. |
| `Production Technical System` → WildFly → Runtime → Standalone Server | Independently operated server runtime. |
| `Production Technical System` → WildFly → Runtime → Managed Server | Domain-managed server runtime. |
| `Production Technical System` → WildFly → Runtime → Process Controller | Process spawning and supervising server processes. |
| `Production Technical System` → WildFly → Runtime → Server Controller | Controller of an individual server runtime. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules | Modular class-loading infrastructure. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Loader | Loads modules and resolves module dependencies. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Dependency Graph | Graph of module visibility/dependency relations. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Class Loader | Class-loading mechanism associated with a module. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Automatic Dependencies | Dependencies automatically added to deployments (Jakarta EE APIs, Weld for CDI, etc.). |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Class Loading Precedence | System Dependencies → User Dependencies → Local Resource → Inter-deployment Dependencies. |
| `Production Technical System` → WildFly → Runtime → Service Container | WildFly's modular service-management infrastructure (MSC). |
| `Production Technical System` → WildFly → Runtime → Service Container → Service | Runtime service registered in the service container. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Dependency | Dependency between runtime services. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Lifecycle | Installation, start, stop and removal of runtime services. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Builder | Fluent API for building service definitions. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Controller | Manages service state transitions. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Registry | Registry of available services. |
| `Production Technical System` → WildFly → Runtime → Request Controller | Runtime mechanism for controlling request processing and concurrency. |
| `Production Technical System` → WildFly → Runtime → Request Flow | Listener to container to application request propagation. |
| `Production Technical System` → WildFly → Runtime → IO / Worker Infrastructure | Runtime I/O and worker-thread infrastructure. |
| `Production Technical System` → WildFly → Runtime → XNIO | Low-level non-blocking I/O and worker infrastructure used by WildFly components. |
| `Production Technical System` → WildFly → Runtime → XNIO → Worker | Thread worker for I/O processing. |
| `Production Technical System` → WildFly → Runtime → XNIO → Channel | I/O channel abstraction. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime | Runtime responsible for processing application deployments. |
| `Production Technical System` → WildFly → Management | Administrative control plane of WildFly. |
| `Production Technical System` → WildFly → Management → Management Model | Structured model representing configurable and runtime resources. |
| `Production Technical System` → WildFly → Management → Management Model → Root Resource | Root of the management-resource tree. |
| `Production Technical System` → WildFly → Management → Management Model → Resource | Addressable management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Attribute | Named property of a management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Operation | Management operation executable against a resource. |
| `Production Technical System` → WildFly → Management → Management Model → Operation Catalog | Catalog of management operation definitions. |
| `Production Technical System` → WildFly → Management → Management Model → Capability | Named capability exposed or required by a management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Capability Reference | Relationship connecting resources through capabilities. |
| `Production Technical System` → WildFly → Management → Management Model → Capability Registry | Registry of exposed and required capabilities. |
| `Production Technical System` → WildFly → Management → Management Model → Address | Ordered list of key/value pairs identifying a resource. |
| `Production Technical System` → WildFly → Management → Management Model → DMR | Detyped Model Representation — the wire format for management operations. |
| `Production Technical System` → WildFly → Management → Management Controller | Component interpreting and executing management operations. |
| `Production Technical System` → WildFly → Management → Operation Dispatch | Controller dispatching operations to runtime services. |
| `Production Technical System` → WildFly → Management → Management Controller → Operation Handler | Mechanism processing a management operation. |
| `Production Technical System` → WildFly → Management → Management Controller → Configuration Persister | Mechanism persisting management-model changes into configuration. |
| `Production Technical System` → WildFly → Management → Management Controller → Model Controller | Controller implementing the management model. |
| `Production Technical System` → WildFly → Management → Management Controller → Audit Logging | Recording of management operations for security and compliance. |
| `Production Technical System` → WildFly → Management → Management Controller → Access Control | Role-based access control for management operations. |
| `Production Technical System` → WildFly → Management → Management Interface | Network interface exposing management operations. |
| `Production Technical System` → WildFly → Management → HTTP Management Interface | HTTP-based management interface (port 9990). |
| `Production Technical System` → WildFly → Management → Native Management Interface | Native management protocol interface (port 9999). |
| `Production Technical System` → WildFly → Management → CLI | Command-line client for management operations. |
| `Production Technical System` → WildFly → Management → CLI → Command | Management command issued by an operator or automation. |
| `Production Technical System` → WildFly → Management → CLI → DMR Request | Detyped Model Representation request sent to the management controller. |
| `Production Technical System` → WildFly → Management → CLI Actuation | Command line encoding operator intent into management operations on the controller. |
| `Production Technical System` → WildFly → Management → Console Actuation | Browser console encoding operator intent into management operations. |
| `Production Technical System` → WildFly → Management → Web Management Interface | Browser-based management interface (HAL). |
| `Production Technical System` → WildFly → Management → JMX Management | JMX-based management integration. |
| `Production Technical System` → WildFly → Management → JMX Management → MBean Server | Runtime registry and access point for MBeans. |
| `Production Technical System` → WildFly → Management → Model Browser | Tool for exploring the management model tree. |
| `Production Technical System` → WildFly → Configuration | Runtime configuration structure. |
| `Production Technical System` → WildFly → Configuration → Extension | Configuration declaration loading a server extension module. |
| `Production Technical System` → WildFly → Configuration → Subsystem | Configurable server subsystem. |
| `Production Technical System` → WildFly → Configuration → Interface | Named network binding interface. |
| `Production Technical System` → WildFly → Configuration → Socket Binding Group | Named collection of socket bindings. |
| `Production Technical System` → WildFly → Configuration → Socket Binding | Named network endpoint binding. |
| `Production Technical System` → WildFly → Configuration → Outbound Socket Binding | Configuration for outbound network connectivity. |
| `Production Technical System` → WildFly → Configuration → System Property | Runtime configuration parameter exposed as a system property. |
| `Production Technical System` → WildFly → Configuration → Environment Variable | External runtime configuration parameter. |
| `Production Technical System` → WildFly → Configuration → Path | Named filesystem path. |
| `Production Technical System` → WildFly → Provisioning | Reproducible construction of server installations. |
| `Production Technical System` → WildFly → Provisioning → Galleon | Provisioning technology used to compose WildFly installations. |
| `Production Technical System` → WildFly → Provisioning → WildFly Galleon Feature Pack | Feature-pack definition supplying WildFly features. |
| `Production Technical System` → WildFly → Provisioning → Feature | Provisionable unit in the feature-pack model. |
| `Production Technical System` → WildFly → Provisioning → Layer | Named compositional server layer. |
| `Production Technical System` → WildFly → Provisioning → Layer Dependency | Dependency between provisioning layers. |
| `Production Technical System` → WildFly → Provisioning → `core-server` Layer | Base server layer. |
| `Production Technical System` → WildFly → Provisioning → `core-tools` Layer | CLI/add-user/Elytron-tool support layer. |
| `Production Technical System` → WildFly → Provisioning → `web-server` Layer | Web-server capability layer. |
| `Production Technical System` → WildFly → Provisioning → `datasources` Layer | Datasource capability layer. |
| `Production Technical System` → WildFly → Provisioning → `jpa` Layer | JPA capability layer. |
| `Production Technical System` → WildFly → Provisioning → `ejb` Layer | Enterprise Beans capability layer. |
| `Production Technical System` → WildFly → Provisioning → `messaging-activemq` Layer | Jakarta Messaging/ActiveMQ Artemis integration layer. |
| `Production Technical System` → WildFly → Provisioning → `jaxrs-server` Layer | Jakarta REST, CDI/JPA and web-server composition layer. |
| `Production Technical System` → WildFly → Provisioning → `ee-core-profile-server` Layer | Jakarta EE Core Profile server composition. |
| `Production Technical System` → WildFly → Provisioning → `cloud-server` Layer | Cloud-oriented server composition layer. |
| `Production Technical System` → WildFly → Provisioning → `health` Layer | Runtime health capability layer. |
| `Production Technical System` → WildFly → Provisioning → `jdr` Layer | Diagnostic-reporting capability layer. |
| `Production Technical System` → WildFly → Provisioning → WildFly Glow | Tooling to identify required Galleon Feature-packs and Layers from application binaries. |
| `Production Technical System` → WildFly → Provisioning → Prospero | Tool for installing and managing updates of WildFly servers. |
| `Production Technical System` → WildFly → Extensions | Extension modules that introduce management resources and runtime services. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.undertow` | Extension implementing Undertow integration. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.messaging-activemq` | Extension implementing ActiveMQ Artemis integration. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.core-management` | Core-management extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.health` | Health subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.metrics` | Metrics subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.config-smallrye` | MicroProfile Config extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.health-smallrye` | MicroProfile Health extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.metrics-smallrye` | MicroProfile Metrics extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.fault-tolerance-smallrye` | MicroProfile Fault Tolerance extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.reactive-messaging-smallrye` | MicroProfile Reactive Messaging extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.microprofile.openapi-smallrye` | MicroProfile OpenAPI extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.clustering.server` | Server-clustering integration. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.elytron` | Elytron security extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.elytron-oidc-client` | Elytron OIDC client extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.io` | I/O subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.remoting` | Remoting subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.transactions` | Transactions subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.batch.jberet` | Batch JBeret extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.bean-validation` | Bean Validation extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.datasources-agroal` | Agroal datasources extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.discovery` | Discovery subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.ee` | EE subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.weld` | CDI/Weld integration extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.ejb3` | EJB3 subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.jaxrs` | JAX-RS subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.jmx` | JMX subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.jpa` | JPA subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.logging` | Logging subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.mail` | Mail subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.naming` | Naming subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.pojo` | POJO subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.security.manager` | Security Manager extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.singleton` | Singleton subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.webservices` | Web Services subsystem extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.mod_cluster` | mod_cluster extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.opentelemetry` | OpenTelemetry extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.micrometer` | Micrometer extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.clustering.ejb` | Distributable EJB clustering extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.clustering.web` | Distributable Web clustering extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.clustering.singleton` | Singleton clustering extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.iiop-openjdk` | IIOP/OpenJDK ORB extension. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.jsf` | JSF extension (Mojarra). |
| `Production Technical System` → WildFly → Subsystems | Collection of server subsystems. |
| `Production Technical System` → WildFly → Subsystems → EE | Jakarta EE integration subsystem. |
| `Production Technical System` → WildFly → Subsystems → EE → Default Bindings | Default Jakarta EE resource bindings. |
| `Production Technical System` → WildFly → Subsystems → EE → Global Modules | Modules made available globally to deployments. |
| `Production Technical System` → WildFly → Subsystems → EE → Concurrency | Jakarta Concurrency integration. |
| `Production Technical System` → WildFly → Subsystems → EE → Managed Executor Service | Managed thread pool executor. |
| `Production Technical System` → WildFly → Subsystems → EE → Managed Scheduled Executor Service | Managed scheduled executor. |
| `Production Technical System` → WildFly → Subsystems → EE → Context Service | Managed context propagation service. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld | Contexts and Dependency Injection runtime integration. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Bean Discovery | Mechanism for discovering CDI beans. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Dependency Injection | Mechanism for resolving and injecting dependencies. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Bean Archive | Archive containing CDI beans. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → `beans.xml` | CDI activation and configuration descriptor. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Producer Method | Method producing CDI-injectable instances. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Interceptor | CDI interceptor binding and implementation. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Decorator | CDI decorator for interface-based enhancement. |
| `Production Technical System` → WildFly → Subsystems → EJB3 | Jakarta Enterprise Beans runtime. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateless Session Bean | Runtime representation of a stateless EJB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateful Session Bean | Runtime representation of a stateful EJB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Singleton Session Bean | Runtime representation of a singleton EJB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Message-Driven Bean | EJB receiving asynchronous messages. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Container | Runtime container for Enterprise Beans. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Pool | Pool of EJB instances. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Remote Invocation | Remote EJB invocation mechanism. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Timer Service | EJB timer runtime. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → `ejb-jar.xml` | EJB deployment descriptor. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → `jboss-ejb3.xml` | WildFly-specific EJB deployment descriptor. |
| `Production Technical System` → WildFly → Subsystems → Naming | JNDI/naming infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace | Namespace containing bound application/server resources. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Binding | Individual name-to-resource binding. |
| `Production Technical System` → WildFly → Subsystems → Naming → Remote Naming | Remote naming access mechanism. |
| `Production Technical System` → WildFly → Subsystems → Undertow | Web-server subsystem. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server | Undertow server resource. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server | Default Undertow server instance. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Host | Virtual host resource. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Host → Default Host | Default virtual host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → HTTP Listener | HTTP endpoint listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → HTTPS Listener | HTTPS/TLS endpoint listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → AJP Listener | AJP endpoint listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container | Servlet runtime container. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet | Servlet runtime component. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Filter | Servlet filter component. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Listener | Servlet context listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket | WebSocket protocol support. |
| `Production Technical System` → WildFly → Subsystems → Undertow → HTTP Invoker | HTTP-based invocation endpoint. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler | Undertow request handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Buffer Pool | Managed buffer pool for I/O. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy | Jakarta REST implementation. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint | Application REST endpoint. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Message Body Reader | HTTP request-body deserialization component. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Message Body Writer | HTTP response-body serialization component. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider | REST content-processing provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Jackson Provider | Jackson JSON REST provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JSON-B Provider | JSON-B REST provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JSON-P Provider | JSON-P REST provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JAXB Provider | JAXB REST provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Exception Mapper | REST exception-to-response mapper. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Client | REST client runtime. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → WebTarget | REST client invocation target. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Subresource | Sub-resource of a REST endpoint. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Request Filter | Client-side REST filter and interceptor. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Client Builder | Builder of REST client instances. |
| `Production Technical System` → WildFly → Subsystems → Datasources | JDBC datasource subsystem. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource | Managed JDBC datasource. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource | XA-capable datasource. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool | Pool of database connections. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JDBC Driver | JDBC driver module/resource. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JNDI Binding | Datasource's JNDI resource binding. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Recovery | XA transaction recovery configuration. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Security Domain | Datasource security domain reference. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation | Connection validation configuration. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Pool Capacity | Configured connection pool size bounds. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Prefill | Connection pool prefill configuration. |
| `Production Technical System` → WildFly → Subsystems → JPA | Jakarta Persistence integration. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit | Deployment-defined persistence configuration. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM | JPA persistence implementation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager | Persistence runtime interface. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache | Persistence caching infrastructure. |
| `Production Technical System` → WildFly → Subsystems → JPA → `persistence.xml` | JPA persistence-unit specification. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache | Shared persistence cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan | Distributed/local caching subsystem. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Container | Logical collection of caches. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Local Cache | Single-node cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache | Distributed cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Replicated Cache | Replicated cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Invalidation Cache | Cache with invalidation semantics. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Persistent Cache | Cache with persistence store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store | Persistence mechanism for cache entries. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Eviction | Cache entry eviction policy. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Expiration | Cache entry expiration policy. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Partition Handling | Partition handling configuration. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Memory Store | Memory and off-heap store configuration. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Indexing | Cache indexing configuration. |
| `Production Technical System` → WildFly → Subsystems → JGroups | Cluster communication subsystem. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel | Logical group-communication channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack | Ordered communication protocol stack. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport | Network transport used by a JGroups channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Properties | Communication protocol properties. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel State | Group-communication channel state. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Receiver | Message receiver of a channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Discovery Protocol | Node discovery protocol. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Failure Detection | Node failure detection mechanism. |
| `Production Technical System` → WildFly → Subsystems → JGroups → MERGE3 | Cluster merge protocol. |
| `Production Technical System` → WildFly → Subsystems → JGroups → FD_SOCK | Socket-based failure detection. |
| `Production Technical System` → WildFly → Subsystems → Clustering | Collection of clustering integrations. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Node | WildFly server participating in a cluster. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership | Relation among participating server nodes. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Distributed Session Management | Mechanism distributing web-session state. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Session Replication Flow | Replication of session state across cluster nodes. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web | Distributed web application/session infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Management | Management of distributable HTTP sessions. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Affinity | Mechanism controlling session-node affinity. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Replication | Mechanism replicating session state. |
| `Production Technical System` → WildFly → Subsystems → Distributable EJB | Distributed EJB state/management infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Singleton | Cluster singleton service infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Service | Service active on one cluster member at a time. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Policy | Policy for singleton election and failover. |
| `Production Technical System` → WildFly → Subsystems → Transactions | Transaction-management subsystem. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager | Coordinates transactions. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Commit Coordination | Coordinator driving participants toward commit. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction | Unit of coordinated resource work. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination | Two-phase transaction coordination mechanism. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery | Transaction recovery mechanism. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store | Persistent transaction log storage. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout | Transaction timeout configuration. |
| `Production Technical System` → WildFly → Subsystems → Transactions → JTS | Java Transaction Service integration. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ | Jakarta Messaging / ActiveMQ Artemis integration. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server | Embedded Artemis messaging server. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address | Artemis message address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue | JMS/Artemis queue. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic | JMS/Artemis topic. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory | JMS connection factory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connector | Messaging network connector. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Remote Connector | Connector to external broker. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Acceptor | Messaging network acceptor. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory | Managed pooled JMS connection factory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge | Bridge between JMS destinations. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting | Messaging security configuration. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting | Per-address configuration. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Redelivery | Message redelivery configuration. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Roles | Messaging security roles. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert | Message diversion rule. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters | Jakarta Connectors resource-adapter integration. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter | Deployable integration component. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition | Resource-adapter connection definition. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → `ra.xml` | Resource-adapter deployment descriptor. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → `ironjacamar.xml` | IronJacamar-specific descriptor. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Admin Object | Resource-adapter administrative object. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Activation | Message-driven activation configuration. |
| `Production Technical System` → WildFly → Subsystems → Security | Legacy security subsystem. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain | Legacy authentication/authorization domain. |
| `Production Technical System` → WildFly → Subsystems → Elytron | Unified WildFly security subsystem. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain | Elytron security-domain configuration. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm | Source of identities/security attributes. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Identity Realm | Realm containing predefined identities. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Filesystem Realm | Realm backed by filesystem data. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JDBC Realm | Realm backed by database queries. |
| `Production Technical System` → WildFly → Subsystems → Elytron → LDAP Realm | Realm backed by LDAP. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JAAS Realm | Realm using JAAS login context. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Aggregate Realm | Composition of multiple realms. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Caching Realm | Realm with identity caching. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store | Cryptographic key-store definition. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Trust Store | Trusted-certificate store. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Credential Store | Secure credential-storage mechanism. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Authentication Factory | Mechanism assembling HTTP/SASL authentication. |
| `Production Technical System` → WildFly → Subsystems → Elytron → HTTP Authentication Factory | HTTP authentication mechanism factory. |
| `Production Technical System` → WildFly → Subsystems → Elytron → SASL Authentication Factory | SASL authentication mechanism factory. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Permission Mapper | Maps identities/roles to permissions. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Role Mapper | Maps roles between security contexts. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Principal Transformer | Transforms security principals. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Evidence Decoder | Decodes authentication evidence. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Realm Mapper | Maps realms across security domains. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration | Centralized SSL/TLS configuration. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Cipher Suite | Configured TLS cipher suite. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Protocol | Configured TLS protocol version. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client | OpenID Connect client integration. |
| `Production Technical System` → WildFly → Subsystems → Web Services | Jakarta XML Web Services integration. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint | SOAP web-service endpoint. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL | Service interface description. |
| `Production Technical System` → WildFly → Subsystems → Web Services → `jboss-webservices.xml` | JBossWS-specific deployment descriptor. |
| `Production Technical System` → WildFly → Subsystems → Web Services → Handler Chain | SOAP handler chain. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret | Jakarta Batch implementation. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job | Batch job definition. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step | Batch processing step. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Repository | Persistent batch job state. |
| `Production Technical System` → WildFly → Subsystems → Mail | Jakarta Mail integration. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session | Configured mail-session resource. |
| `Production Technical System` → WildFly → Subsystems → JMX | Java Management Extensions integration. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean | Managed Java object. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Server | Runtime registry and access point for MBeans. |
| `Production Technical System` → WildFly → Subsystems → JMX → JMX Connector | Remote JMX access connector. |
| `Production Technical System` → WildFly → Subsystems → Logging | Server logging infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category | Named logging category. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler | Log output handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → File Handler | File-based logging handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → Console Handler | Console logging handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → Periodic Rotating File Handler | Time-based rotating file handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → Size Rotating File Handler | Size-based rotating file handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → Async Handler | Asynchronous logging handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → Formatter | Log-message formatting mechanism. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Level | Severity filtering threshold. |
| `Production Technical System` → WildFly → Subsystems → IO | I/O subsystem. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker | Thread worker resource. |
| `Production Technical System` → WildFly → Subsystems → IO → Buffer Pool | Managed buffer resource. |
| `Production Technical System` → WildFly → Subsystems → Remoting | Remote communication infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Connector | Remote communication connector. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Endpoint | Remoting endpoint. |
| `Production Technical System` → WildFly → Subsystems → Remoting → HTTP Upgrade | HTTP-upgrade-based remoting. |
| `Production Technical System` → WildFly → Subsystems → Remoting → SASL Policy | SASL authentication policy for remoting. |
| `Production Technical System` → WildFly → Subsystems → Discovery | Service discovery infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Discovery Provider | Provider used to locate remote services. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Static Discovery | Static list-based discovery. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Aggregate Discovery | Composite discovery provider. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster | Dynamic load-balancing integration. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Proxy | Front-end load-balancing proxy. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise | Cluster advertisement mechanism. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Balancer | Load-balancing policy. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Node | Cluster node registration. |
| `Production Technical System` → WildFly → Subsystems → Health | Runtime health-check subsystem. |
| `Production Technical System` → WildFly → Subsystems → Health → Health Check | Runtime health evaluation. |
| `Production Technical System` → WildFly → Subsystems → Health → Readiness Check | Kubernetes readiness probe. |
| `Production Technical System` → WildFly → Subsystems → Health → Liveness Check | Kubernetes liveness probe. |
| `Production Technical System` → WildFly → Subsystems → Metrics | Runtime metrics infrastructure. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Metric | Measured runtime property. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Gauge | Point-in-time metric. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Counter | Monotonically increasing metric. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Histogram | Distribution metric. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile | MicroProfile capability collection. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Config | Externalized configuration capability. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Health | Application health capability. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance | Fault-tolerance mechanisms. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Reactive Messaging | Reactive messaging capability. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Metrics | Application/runtime metrics capability. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI | API documentation generation. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT | JWT authentication capability. |
| `Production Technical System` → WildFly → Subsystems → SAR | Service Archive deployment subsystem. |
| `Production Technical System` → WildFly → Subsystems → SAR → SAR Deployment | Service Archive deployment. |
| `Production Technical System` → WildFly → Subsystems → SAR → MBean | MBean supplied by SAR deployment. |
| `Production Technical System` → WildFly → Subsystems → JSF | Jakarta Server Faces integration. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra | JSF implementation. |
| `Production Technical System` → WildFly → Subsystems → JSF → `faces-config.xml` | JSF configuration descriptor. |
| `Production Technical System` → WildFly → Subsystems → POJO | Plain Old Java Object subsystem. |
| `Production Technical System` → WildFly → Subsystems → POJO → POJO Deployment | POJO deployment unit. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation | Jakarta Bean Validation integration. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Validator | Bean validation runtime. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint | Validation constraint definition. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner | Filesystem-based deployment detection. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Scan Interval | Deployment directory polling interval. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Auto-Deploy | Automatic deployment configuration. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Deployment Marker | Marker controlling scanner deployment state. |
| `Production Technical System` → WildFly → Deployment | Application deployment system. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit | Unit submitted to WildFly for deployment. |
| `Production Technical System` → WildFly → Deployment → Subdeployment | Nested deployment within an enterprise archive. |
| `Production Technical System` → WildFly → Deployment → Resource Root | Resource root of a deployment unit. |
| `Production Technical System` → WildFly → Deployment → Deployment Overlay | Overlay altering deployment content without repackaging. |
| `Production Technical System` → WildFly → Deployment → Deployment Structure | Structural organization of deployment content. |
| `Production Technical System` → WildFly → Deployment → WAR | Web application deployment archive. |
| `Production Technical System` → WildFly → Deployment → JAR | Java/application module deployment archive. |
| `Production Technical System` → WildFly → Deployment → EAR | Enterprise application archive. |
| `Production Technical System` → WildFly → Deployment → RAR | Resource-adapter archive. |
| `Production Technical System` → WildFly → Deployment → SAR | Service Archive deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Descriptor | Declarative deployment configuration. |
| `Production Technical System` → WildFly → Deployment → `web.xml` | Servlet deployment descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-web.xml` | WildFly web-deployment descriptor. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` | EJB deployment descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-ejb3.xml` | WildFly EJB deployment descriptor. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` | JPA persistence-unit specification. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` | CDI activation descriptor. |
| `Production Technical System` → WildFly → Deployment → `application.xml` | Java EE application descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-app.xml` | JBoss application descriptor. |
| `Production Technical System` → WildFly → Deployment → `ra.xml` | Resource adapter descriptor. |
| `Production Technical System` → WildFly → Deployment → `ironjacamar.xml` | IronJacamar descriptor. |
| `Production Technical System` → WildFly → Deployment → `application-client.xml` | Application client descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-client.xml` | JBoss application client descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` | Class-loading control descriptor. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation | Annotation contributing deployment metadata. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor | Component processing deployment metadata/content. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase | Ordered stage of deployment processing. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit Processor | Processor transforming deployment state during deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Service | Runtime service representing deployed application state. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle | Deploy, undeploy, redeploy, replace and related transitions. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner | Filesystem-based deployment detection mechanism. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Deployment Marker | Marker controlling scanner deployment state. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker | Marker controlling scanner deployment state. |
| `Production Technical System` → WildFly → Deployment → Application | Application deployed into WildFly. |
| `Production Technical System` → WildFly → Deployment → Application → Module | Application module within an application deployment. |
| `Production Technical System` → WildFly → Deployment → Application → Component | Deployable application component. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet | Deployed servlet component. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean | Deployed CDI component. |
| `Production Technical System` → WildFly → Deployment → Application → EJB | Deployed Enterprise Bean. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource | Deployed REST resource. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit | Deployed persistence unit. |
| `Production Technical System` → WildFly → Deployment → Application → JNDI Resource | Application-visible resource binding. |
| `Production Technical System` → WildFly → Deployment → Application → Security Domain Association | Application-to-security-domain relation. |
| `Production Technical System` → WildFly → Deployment → Application → Datasource Dependency | Application-to-datasource relation. |
| `Production Technical System` → WildFly → Deployment → Application → Messaging Dependency | Application-to-messaging resource relation. |
| `Production Technical System` → WildFly → Deployment → Application → Module Dependency | Application module dependency on WildFly module. |
| `Production Technical System` → WildFly → Network | Network-facing technical structure. |
| `Production Technical System` → WildFly → Network → Public Interface | Interface exposed for application traffic. |
| `Production Technical System` → WildFly → Network → Management Interface | Interface exposed for administration. |
| `Production Technical System` → WildFly → Network → Unsecure Interface | Interface for unsecured traffic. |
| `Production Technical System` → WildFly → Network → HTTP Endpoint | HTTP application endpoint. |
| `Production Technical System` → WildFly → Network → HTTPS Endpoint | HTTPS/TLS application endpoint. |
| `Production Technical System` → WildFly → Network → AJP Endpoint | AJP application endpoint. |
| `Production Technical System` → WildFly → Network → Remoting Endpoint | Remote invocation endpoint. |
| `Production Technical System` → WildFly → Network → Messaging Endpoint | Messaging endpoint. |
| `Production Technical System` → WildFly → Network → JGroups Endpoint | Cluster communication endpoint. |
| `Production Technical System` → WildFly → Network → TXN Recovery Endpoint | Transaction recovery endpoint. |
| `Production Technical System` → WildFly → Network → TXN Status Manager Endpoint | Transaction status manager endpoint. |
| `Production Technical System` → WildFly → Network → Management HTTP Endpoint | Management HTTP endpoint (9990). |
| `Production Technical System` → WildFly → Network → Management Native Endpoint | Management native endpoint (9999). |
| `Production Technical System` → WildFly → Network → Socket Binding | Named socket binding with port and interface. |
| `Production Technical System` → WildFly → Network → Socket Binding Group | Named collection of socket bindings. |
| `Production Technical System` → WildFly → Network → Port Offset | Offset applied to all socket bindings. |
| `Production Technical System` → WildFly → Network → Outbound Socket Binding | Configuration for outbound connectivity. |
| `Production Technical System` → WildFly → Network → Client Mapping | Client-side address mapping for a socket binding. |
| `Production Technical System` → WildFly → Network → Interface Criteria | Address selection rules for a network interface. |
| `Production Technical System` → WildFly → Runtime Security | Runtime security structure. |
| `Production Technical System` → WildFly → Runtime Security → Authentication | Identity verification capability. |
| `Production Technical System` → WildFly → Runtime Security → Authorization | Permission-decision capability. |
| `Production Technical System` → WildFly → Runtime Security → TLS | Transport-security mechanism. |
| `Production Technical System` → WildFly → Runtime Security → Credential Store | Secure credential storage. |
| `Production Technical System` → WildFly → Runtime Security → Identity | Security identity representation. |
| `Production Technical System` → WildFly → Runtime Security → Principal | Security principal representation. |
| `Production Technical System` → WildFly → Runtime Security → Role | Authorization-role representation. |
| `Production Technical System` → WildFly → Runtime Security → Permission | Authorization permission representation. |
| `Production Technical System` → WildFly → Runtime Security → Security Event | Security-related runtime event. |
| `Production Technical System` → WildFly → Runtime Security → Audit Event | Auditable security event. |
| `Production Technical System` → WildFly → Runtime Security → Security Domain | Runtime security domain. |
| `Production Technical System` → WildFly → Runtime Security → Realm | Runtime security realm. |
| `Production Technical System` → WildFly → Runtime Security → SSL Context | Runtime SSL/TLS context. |
| `Production Technical System` → WildFly → Runtime Control | Runtime control and observability structure. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State | Current server configuration state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State | Current runtime state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric | Quantitative runtime observation. |
| `Production Technical System` → WildFly → Runtime Control → Log Event | Recorded runtime event. |
| `Production Technical System` → WildFly → Runtime Control → Health Result | Result of a health evaluation. |
| `Production Technical System` → WildFly → Runtime Control → Diagnostic Report | Consolidated diagnostic information. |
| `Production Technical System` → WildFly → Runtime Control → JDR | JBoss Diagnostic Reporting mechanism. |
| `Production Technical System` → WildFly → Runtime Control → Audit Log | Management audit trail. |
| `Production Technical System` → WildFly → Runtime Control → Server Log | Server runtime log. |
| `Production Technical System` → WildFly → Runtime Control → GC Log | Garbage collection log. |
| `Production Technical System` → WildFly → Runtime Control → Thread Dump | Thread state snapshot. |
| `Production Technical System` → WildFly → Runtime Control → Heap Dump | Memory state snapshot. |
| `Production Technical System` → WildFly → Lifecycle | WildFly technical lifecycle. |
| `Production Technical System` → WildFly → Lifecycle → Provision | Construction of a WildFly installation. |
| `Production Technical System` → WildFly → Lifecycle → Install | Installation of WildFly distribution. |
| `Production Technical System` → WildFly → Lifecycle → Configure | Establishment of server configuration. |
| `Production Technical System` → WildFly → Lifecycle → Start | Creation and activation of runtime services. |
| `Production Technical System` → WildFly → Lifecycle → Boot | Initialization of server runtime. |
| `Production Technical System` → WildFly → Lifecycle → Deploy | Introduction of application deployment into runtime. |
| `Production Technical System` → WildFly → Lifecycle → Redeploy | Replacement/reprocessing of deployment. |
| `Production Technical System` → WildFly → Lifecycle → Reload | Reinitialization of server configuration/runtime. |
| `Production Technical System` → WildFly → Lifecycle → Shutdown | Controlled termination of server runtime. |
| `Production Technical System` → WildFly → Lifecycle → Undeploy | Removal of application deployment. |
| `Production Technical System` → WildFly → Lifecycle → Maintain | Continued corrective/preventive technical work. |
| `Production Technical System` → WildFly → Lifecycle → Patch | Application of a server update/patch. |
| `Production Technical System` → WildFly → Lifecycle → Upgrade | Transition to a newer WildFly version. |
| `Production Technical System` → WildFly → Lifecycle → Migrate | Transition from an older technical configuration/version. |
| `Production Technical System` → WildFly → Lifecycle → Retire | Removal of WildFly from technical service. |
| `Production Technical System` → WildFly → Lifecycle → Rollback | Reversion to a previous configuration/version. |
| `Production Technical System` → WildFly → Lifecycle → Backup | Preservation of configuration and data state. |
| `Production Technical System` → WildFly → Lifecycle → Restore | Recovery from a preserved state. |
| `Production Technical System` → WildFly → External Resources | External resources on which WildFly depends. |
| `Production Technical System` → WildFly → External Resources → CPU | Processing resource. |
| `Production Technical System` → WildFly → External Resources → Memory | Runtime memory resource. |
| `Production Technical System` → WildFly → External Resources → Filesystem | Persistent storage resource. |
| `Production Technical System` → WildFly → External Resources → Network | Network resource. |
| `Production Technical System` → WildFly → External Resources → Database | External persistence resource. |
| `Production Technical System` → WildFly → External Resources → Message Broker | External messaging resource where remote messaging is configured. |
| `Production Technical System` → WildFly → External Resources → Identity Provider | External identity source (e.g., Keycloak, LDAP). |
| `Production Technical System` → WildFly → External Resources → Certificate Authority | External trust infrastructure. |
| `Production Technical System` → WildFly → External Resources → Load Balancer | External traffic-routing infrastructure (e.g., mod_cluster, HAProxy). |
| `Production Technical System` → WildFly → External Resources → JDK | External Java runtime. |
| `Production Technical System` → WildFly → External Resources → Operating System | External OS facilities. |
| `Production Technical System` → WildFly → External Resources → Container Runtime | Docker/Podman runtime where containerized. |
| `Production Technical System` → WildFly → External Resources → Kubernetes | Kubernetes orchestration environment. |
| `Production Technical System` → WildFly → External Resources → DNS | External name-resolution resource. |
| `Production Technical System` → WildFly → External Resources → NTP | External time-synchronization resource. |
| `Production Technical System` → WildFly → External Resources → Storage Devices | External block and file storage devices. |
| `Production Technical System` → WildFly → External Resources → Network Devices | External network devices. |
| `Production Technical System` → WildFly → Technical Standards | Standards implemented or integrated by WildFly. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta EE | Enterprise Java platform specification family implemented by WildFly. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Servlet | Web application programming model. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta REST | RESTful web-service specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Enterprise Beans | Enterprise component specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Persistence | Persistence specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Messaging | Messaging specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta CDI | Dependency-injection/context specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Transactions | Transaction specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Bean Validation | Bean validation specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Batch | Batch processing specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Concurrency | Concurrency utilities specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Connectors | Resource adapter specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Mail | Mail specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta WebSocket | WebSocket specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Binding | JSON-B specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Processing | JSON-P specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Binding | JAXB specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Web Services | JAX-WS specification. |
| `Production Technical System` → WildFly → Technical Standards → JDBC | Java database-connectivity standard/API. |
| `Production Technical System` → WildFly → Technical Standards → JNDI | Naming API/model. |
| `Production Technical System` → WildFly → Technical Standards → JMX | Java management standard/API. |
| `Production Technical System` → WildFly → Technical Standards → HTTP | Application/network protocol. |
| `Production Technical System` → WildFly → Technical Standards → HTTPS | Secure HTTP protocol. |
| `Production Technical System` → WildFly → Technical Standards → TLS | Transport-security protocol. |
| `Production Technical System` → WildFly → Technical Standards → AJP | Apache JServ Protocol. |
| `Production Technical System` → WildFly → Technical Standards → WebSocket | WebSocket protocol. |
| `Production Technical System` → WildFly → Technical Standards → OIDC | OpenID Connect. |
| `Production Technical System` → WildFly → Technical Standards → OAuth 2.0 | Authorization framework. |
| `Production Technical System` → WildFly → Technical Standards → SAML | Security Assertion Markup Language. |
| `Production Technical System` → WildFly → Technical Standards → JWT | JSON Web Token. |
| `Production Technical System` → WildFly → Technical Standards → MicroProfile | MicroProfile specification family. |
| `Production Technical System` → WildFly → Technical Standards → OpenAPI | API description standard. |
| `Production Technical System` → WildFly → Technical Standards → OpenTelemetry | Observability standard. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Security | Jakarta Security specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Authentication | Jakarta Authentication specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Authorization | Jakarta Authorization specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Faces | Jakarta Faces specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Server Pages | Jakarta Server Pages specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Expression Language | Jakarta Expression Language specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Interceptors | Jakarta Interceptors specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Dependency Injection | Jakarta Dependency Injection specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Activation | Jakarta Activation specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Management | Jakarta Management specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Deployment | Jakarta Deployment specification. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Annotations | Jakarta Annotations specification. |
| `Production Technical System` → WildFly → Technical Standards → SOAP | SOAP messaging protocol. |
| `Production Technical System` → WildFly → Technical Standards → XML-RPC | XML-RPC protocol. |
| `Production Technical System` → WildFly → Technical Practices | Repeatable practices used to operate and maintain WildFly. |
| `Production Technical System` → WildFly → Technical Practices → Provisioning | Reproducible server construction. |
| `Production Technical System` → WildFly → Technical Practices → Configuration Management | Controlled management of server configuration. |
| `Production Technical System` → WildFly → Technical Practices → Application Deployment | Controlled introduction of applications. |
| `Production Technical System` → WildFly → Technical Practices → Monitoring | Observation of runtime state and performance. |
| `Production Technical System` → WildFly → Technical Practices → Health Checking | Periodic/evaluative checking of runtime health. |
| `Production Technical System` → WildFly → Technical Practices → Log Analysis | Analysis of generated runtime records. |
| `Production Technical System` → WildFly → Technical Practices → Backup / Recovery | Preservation and restoration of required technical state. |
| `Production Technical System` → WildFly → Technical Practices → Patching | Application of maintenance updates. |
| `Production Technical System` → WildFly → Technical Practices → Capacity Management | Management of resource capacity and limits. |
| `Production Technical System` → WildFly → Technical Practices → Security Hardening | Reduction of unnecessary exposure and configuration risk. |
| `Production Technical System` → WildFly → Technical Practices → Performance Tuning | Optimization of runtime performance characteristics. |
| `Production Technical System` → WildFly → Technical Practices → Thread Management | Configuration and tuning of thread pools. |
| `Production Technical System` → WildFly → Technical Practices → Connection Pool Tuning | Optimization of datasource connection pools. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning | Optimization of JVM heap, GC, and system properties. |
| `Production Technical System` → WildFly → Technical Practices → Incident Management | Handling of runtime incidents. |
| `Production Technical System` → WildFly → Technical Practices → Problem Management | Analysis of recurring technical problems. |
| `Production Technical System` → WildFly → Technical Practices → Change Management | Controlled introduction of configuration changes. |
| `Production Technical System` → WildFly → Technical Practices → Release Management | Planning and control of server releases. |
| `Production Technical System` → WildFly → Technical Practices → Compliance Management | Assurance of regulatory and policy compliance. |
| `Production Technical System` → WildFly → Technical Practices → Disaster Recovery | Restoration of service after catastrophic failure. |
| `Production Technical System` → WildFly → Technical Practices → Cost Management | Management of operational resource costs. |
| `Production Technical System` → WildFly → Technical Dependencies | External and internal dependencies of WildFly. |
| `Production Technical System` → WildFly → Technical Dependencies → JVM | WildFly requires a compatible Java runtime. |
| `Production Technical System` → WildFly → Technical Dependencies → Operating System | Runtime depends on OS facilities. |
| `Production Technical System` → WildFly → Technical Dependencies → Filesystem | Runtime depends on filesystem access. |
| `Production Technical System` → WildFly → Technical Dependencies → Network Stack | Runtime communication depends on network facilities. |
| `Production Technical System` → WildFly → Technical Dependencies → Database | Datasource/JPA applications may depend on databases. |
| `Production Technical System` → WildFly → Technical Dependencies → External Services | Applications/server features may depend on external services. |
| `Production Technical System` → WildFly → Technical Dependencies → Message Broker | Remote messaging depends on external broker. |
| `Production Technical System` → WildFly → Technical Dependencies → Identity Provider | Security depends on external identity source. |
| `Production Technical System` → WildFly → Technical Dependencies → Certificate Authority | TLS depends on external trust infrastructure. |
| `Production Technical System` → WildFly → Technical Dependencies → Load Balancer | Cluster traffic routing depends on external LB. |
| `Production Technical System` → WildFly → Technical Dependencies → Container Runtime | Containerized deployment depends on Docker/Podman. |
| `Production Technical System` → WildFly → Technical Dependencies → Kubernetes API | Kubernetes deployment depends on API server. |
| `Production Technical System` → WildFly → Technical Dependencies → OS Packages | Runtime depends on operating-system packages. |
| `Production Technical System` → WildFly → Technical Dependencies → DNS | Name resolution depends on external DNS. |
| `Production Technical System` → WildFly → Technical Dependencies → NTP | Time synchronization depends on external NTP. |
| `Production Technical System` → WildFly → Technical Dependencies → External Monitoring | Observability depends on external monitoring and logging systems. |
| `Production Technical System` → WildFly → Technical Control | Control and observability structure of this WildFly instance. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite | Determination that configuration/deployment satisfies specified conditions. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite | Determination that the deployed system fulfills its intended technical purpose. |
| `Production Technical System` → WildFly → Technical Control → Feedback | Logs, metrics, health and management state returned from runtime. |
| `Production Technical System` → WildFly → Technical Control → Failure | Runtime failure of a component/service/deployment. |
| `Production Technical System` → WildFly → Technical Control → Hazard | Condition capable of causing undesirable technical consequences. |
| `Production Technical System` → WildFly → Technical Control → Risk | Possibility and consequence of an undesirable technical event. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off | Configuration/design compromise among competing technical properties. |
| `Production Technical System` → WildFly → Technical Control → Performance | Runtime response, throughput, resource consumption and related measurements. |
| `Production Technical System` → WildFly → Technical Control → Availability | Runtime uptime and accessibility. |
| `Production Technical System` → WildFly → Technical Control → Throughput | Requests processed per unit time. |
| `Production Technical System` → WildFly → Technical Control → Latency | Response time distribution. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization | CPU, memory, disk, network consumption. |
| `Production Technical System` → WildFly → Technical Control → Error Rate | Frequency of failed requests/operations. |
| `Production Technical System` → WildFly → Technical Control → Saturation | Degree of resource saturation. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.sh` → JVM Launch | Invocation of the Java runtime with standalone parameters. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.sh` → Classpath Setup | Construction of the runtime classpath from modules and boot libraries. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.sh` → Module Path Configuration | Configuration of the JBoss Modules path for the runtime. |
| `Production Technical System` → WildFly → Distribution → `bin/standalone.sh` → Main Class Invocation | Invocation of the WildFly bootstrap main class. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.sh` → Host Controller Launch | Invocation of the Host Controller process. |
| `Production Technical System` → WildFly → Distribution → `bin/domain.sh` → Domain Controller Connection | Establishment of connection to the Domain Controller. |
| `Production Technical System` → WildFly → Distribution → `bin/jboss-cli.sh` → CLI Bootstrap | Initialization of the management CLI client. |
| `Production Technical System` → WildFly → Distribution → `bin/jboss-cli.sh` → Connection Establishment | Connection of the CLI to a management endpoint. |
| `Production Technical System` → WildFly → Distribution → `bin/add-user.sh` → User Creation | Interactive or batch creation of a management/application user. |
| `Production Technical System` → WildFly → Distribution → `bin/add-user.sh` → Credential Hashing | Hashing of the user password for storage. |
| `Production Technical System` → WildFly → Distribution → `bin/add-user.sh` → Property File Update | Update of the users/groups properties files. |
| `Production Technical System` → WildFly → Distribution → `bin/elytron-tool.sh` → Keystore Generation | Generation of a cryptographic keystore. |
| `Production Technical System` → WildFly → Distribution → `bin/elytron-tool.sh` → Credential Store Generation | Generation of a credential store. |
| `Production Technical System` → WildFly → Distribution → `modules → Module → module.xml` → Dependencies Declaration | Declaration of module dependencies. |
| `Production Technical System` → WildFly → Distribution → `modules → Module → module.xml` → Resources Declaration | Declaration of module resources and exports. |
| `Production Technical System` → WildFly → Distribution → `modules → Module → module.xml` → Main Class Declaration | Declaration of the module main class. |
| `Production Technical System` → WildFly → Distribution → `modules → Module → module.xml` → Properties Declaration | Declaration of module properties and aliases. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Extensions Section | Declarations of loaded server extensions. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Management Section | Management interface and security-realm configuration. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Profile Section | Subsystem configuration for the active profile. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Interfaces Section | Named interface declarations. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Socket Binding Groups Section | Named socket-binding groups. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Deployment Scanner Section | Deployment-scanner configuration. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → System Properties Section | System-property declarations. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Paths Section | Named filesystem path declarations. |
| `Production Technical System` → WildFly → Distribution → `standalone/configuration/standalone.xml` → Management Users | Management user/group references. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` → Profiles Section | Domain-wide subsystem profiles. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` → Server Groups Section | Named server groups. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` → Socket Binding Groups Section | Domain-wide socket-binding groups. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` → Hosts Section | Declared host controllers. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/domain.xml` → Server Configurations Section | Per-server configuration entries. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → Host Identity | Host controller identity. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → Domain Controller Reference | Reference to the domain controller. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → Local Server Configuration | Locally managed server configuration. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → JVM Configuration | JVM launch options per server. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → Interface Configuration | Host-level interface declarations. |
| `Production Technical System` → WildFly → Domain Distribution → `domain/configuration/host.xml` → Socket Binding Group | Host-level socket-binding group. |
| `Production Technical System` → WildFly → Domain Distribution → Host Controller → Registration | Registration of the host with the Domain Controller. |
| `Production Technical System` → WildFly → Domain Distribution → Host Controller → Process Supervision | Supervision of the managed server processes. |
| `Production Technical System` → WildFly → Domain Distribution → Host Controller → Configuration Propagation | Propagation of domain configuration to servers. |
| `Production Technical System` → WildFly → Domain Distribution → Domain Controller → Central Configuration | Central management of domain configuration. |
| `Production Technical System` → WildFly → Domain Distribution → Domain Controller → Server Group Management | Management of server groups across hosts. |
| `Production Technical System` → WildFly → Domain Distribution → Domain Controller → Deployment Distribution | Distribution of deployments to server groups. |
| `Production Technical System` → WildFly → Domain Distribution → Server Group → Profile Assignment | Association of a profile with a server group. |
| `Production Technical System` → WildFly → Domain Distribution → Server Group → Socket Binding Group Assignment | Association of a socket-binding group with a server group. |
| `Production Technical System` → WildFly → Domain Distribution → Server Group → JVM Assignment | Association of JVM settings with a server group. |
| `Production Technical System` → WildFly → Domain Distribution → Domain Formation | Constituting a managed domain from hosts, groups, and profiles. |
| `Production Technical System` → WildFly → Runtime → JVM → Heap | JVM heap memory regions. |
| `Production Technical System` → WildFly → Runtime → JVM → Metaspace | JVM metaspace region. |
| `Production Technical System` → WildFly → Runtime → JVM → Thread Stacks | Per-thread JVM stacks. |
| `Production Technical System` → WildFly → Runtime → JVM → GC | Garbage collector subsystem. |
| `Production Technical System` → WildFly → Runtime → JVM → Class Loader Subsystem | JVM class-loading subsystem. |
| `Production Technical System` → WildFly → Runtime → JVM → JIT Compiler | Just-in-time compiler. |
| `Production Technical System` → WildFly → Runtime → JVM → JNI | Java Native Interface. |
| `Production Technical System` → WildFly → Runtime → Java Process → Process Descriptor | OS process descriptor. |
| `Production Technical System` → WildFly → Runtime → Java Process → Thread Pools | OS-level threads backing the runtime. |
| `Production Technical System` → WildFly → Runtime → Java Process → File Descriptors | Open file descriptors. |
| `Production Technical System` → WildFly → Runtime → Java Process → Signal Handlers | Handlers for OS signals. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Repository | Repository of installed modules. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Index | Index of modules by name. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Local Loader | Loader for local module resources. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Resource Loader | Loader for module resources. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Loader → Dependency Resolution | Algorithm resolving module dependencies. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Loader → Module Linking | Linking of modules into the runtime graph. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Class Loader → Parent Delegation | Delegation policy to parent class loader. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Module Class Loader → Resource Visibility | Visibility rules for module resources. |
| `Production Technical System` → WildFly → Runtime → JBoss Modules → Modular Class Loading | Loading isolated modules with dependency resolution and delegation. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Installation | Installation of services into the container. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Start | Start of installed services. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Stop | Stop of running services. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Removal | Removal of services from the container. |
| `Production Technical System` → WildFly → Runtime → Service Container → Dependency Resolution | Resolution of inter-service dependencies. |
| `Production Technical System` → WildFly → Runtime → Service Container → State Transition | Controlled service state transition. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Registry → Lookup | Lookup of services by name. |
| `Production Technical System` → WildFly → Runtime → Service Container → Service Lifecycle Management | Installing, starting, stopping, and removing services in dependency order. |
| `Production Technical System` → WildFly → Runtime → Request Controller → Request Queue | Queue of pending requests. |
| `Production Technical System` → WildFly → Runtime → Request Controller → Concurrency Control | Control of request concurrency. |
| `Production Technical System` → WildFly → Runtime → Request Controller → Backpressure | Backpressure handling. |
| `Production Technical System` → WildFly → Runtime → XNIO → Selector | I/O selector for readiness events. |
| `Production Technical System` → WildFly → Runtime → XNIO → Channel Listener | Listener for I/O channel events. |
| `Production Technical System` → WildFly → Runtime → XNIO → Worker Task Queue | Queue of tasks for worker threads. |
| `Production Technical System` → WildFly → Runtime → XNIO → Worker Thread Pool | Pool of I/O worker threads. |
| `Production Technical System` → WildFly → Runtime → XNIO → Asynchronous Dispatch | Handing I/O work to workers and selectors without blocking. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime → Deployment Processor Chain | Chain of processors applied to deployments. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime → Deployment Repository | Repository of deployed content realized through computation. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime → VFS | Virtual file system for deployment content realized through computation. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime → Runtime Stage | Runtime-stage deployment processing. |
| `Production Technical System` → WildFly → Runtime → Deployment Runtime → Staged Deployment Processing | Transforming deployment content into runtime services through ordered stages. |
| `Production Technical System` → WildFly → Management → Management Model → Root Resource → Host | Host-level management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Root Resource → Server | Server-level management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Root Resource → Deployment | Deployment management resource. |
| `Production Technical System` → WildFly → Management → Management Model → Resource → Address | Address identifying the resource. |
| `Production Technical System` → WildFly → Management → Management Model → Resource → Attributes | Attributes of the resource. |
| `Production Technical System` → WildFly → Management → Management Model → Resource → Operations | Operations on the resource. |
| `Production Technical System` → WildFly → Management → Management Model → Resource → Children | Child resources. |
| `Production Technical System` → WildFly → Management → Management Model → Attribute → Value Type | Type of the attribute value. |
| `Production Technical System` → WildFly → Management → Management Model → Attribute → Access Type | Read/write/read-only access. |
| `Production Technical System` → WildFly → Management → Management Model → Attribute → Default Value | Default attribute value. |
| `Production Technical System` → WildFly → Management → Management Model → Operation → Operation Signature | Signature of the operation. |
| `Production Technical System` → WildFly → Management → Management Model → Operation → Operation Handler | Handler executing the operation. |
| `Production Technical System` → WildFly → Management → Management Model → Operation → Result | Result returned by the operation. |
| `Production Technical System` → WildFly → Management → Management Controller → Model Controller → Model Registration | Registration of resources in the model. |
| `Production Technical System` → WildFly → Management → Management Controller → Model Controller → Model Traversal | Traversal of the model tree. |
| `Production Technical System` → WildFly → Management → Management Controller → Model Controller → Model Validation | Validation of model changes. |
| `Production Technical System` → WildFly → Management → Management Controller → Configuration Persister → XML Serialization | Serialization of model to XML. |
| `Production Technical System` → WildFly → Management → Management Controller → Configuration Persister → XML Deserialization | Deserialization of model from XML. |
| `Production Technical System` → WildFly → Management → Management Controller → Configuration Persister → Backup | Backup of persisted configuration. |
| `Production Technical System` → WildFly → Management → Management Controller → Audit Logging → Event Record | Recording of management events. |
| `Production Technical System` → WildFly → Management → Management Controller → Audit Logging → Log Rotation | Rotation of audit logs. |
| `Production Technical System` → WildFly → Management → Management Controller → Access Control → Role Assignment | Assignment of roles to identities. |
| `Production Technical System` → WildFly → Management → Management Controller → Access Control → Permission Check | Check of operation permissions. |
| `Production Technical System` → WildFly → Management → HTTP Management Interface → HTTP Endpoint | HTTP listener for management. |
| `Production Technical System` → WildFly → Management → HTTP Management Interface → JSON Encoding | JSON encoding of DMR. |
| `Production Technical System` → WildFly → Management → HTTP Management Interface → Authentication | HTTP authentication for management. |
| `Production Technical System` → WildFly → Management → HTTP Management Interface → Console | HAL management console. |
| `Production Technical System` → WildFly → Management → Native Management Interface → Native Protocol | Native management protocol. |
| `Production Technical System` → WildFly → Management → Native Management Interface → SASL Authentication | SASL-based authentication for native management. |
| `Production Technical System` → WildFly → Management → CLI → Command → Connect Command | CLI connect command. |
| `Production Technical System` → WildFly → Management → CLI → Command → Read Command | CLI read-attribute/read-resource command. |
| `Production Technical System` → WildFly → Management → CLI → Command → Write Command | CLI write-attribute command. |
| `Production Technical System` → WildFly → Management → CLI → Command → Operation Command | CLI :operation command. |
| `Production Technical System` → WildFly → Management → CLI → Command → Deploy Command | CLI deploy/undeploy command. |
| `Production Technical System` → WildFly → Management → CLI → Command → Batch Command | CLI batch command. |
| `Production Technical System` → WildFly → Management → CLI → Batch Execution | Situated batch execution of management commands. |
| `Production Technical System` → WildFly → Management → CLI → DMR Request → Request Encoding | Encoding of DMR request. |
| `Production Technical System` → WildFly → Management → CLI → DMR Request → Response Handling | Handling of DMR response. |
| `Production Technical System` → WildFly → Management → Web Management Interface → HAL Console | HAL web console. |
| `Production Technical System` → WildFly → Management → Web Management Interface → REST Endpoint | REST endpoint for management. |
| `Production Technical System` → WildFly → Management → JMX Management → MBean Server → Registration | Registration of MBeans. |
| `Production Technical System` → WildFly → Management → JMX Management → MBean Server → Query | JMX query processing. |
| `Production Technical System` → WildFly → Management → JMX Management → MBean Server → Notification | JMX notification delivery. |
| `Production Technical System` → WildFly → Management → Model Browser → Tree Navigation | Navigation of the management model tree. |
| `Production Technical System` → WildFly → Management → Model Browser → Attribute Inspection | Inspection of resource attributes. |
| `Production Technical System` → WildFly → Management → Detyped Model Manipulation | Managing resources as DMR address, attribute, and operation trees. |
| `Production Technical System` → WildFly → Configuration → Extension → Module Reference | Reference to the extension module. |
| `Production Technical System` → WildFly → Configuration → Extension → Subsystem Registration | Registration of extension subsystems. |
| `Production Technical System` → WildFly → Configuration → Subsystem → Resource Definition | Definition of subsystem resources. |
| `Production Technical System` → WildFly → Configuration → Subsystem → Operation Definition | Definition of subsystem operations. |
| `Production Technical System` → WildFly → Configuration → Subsystem → Capability Declaration | Declaration of subsystem capabilities. |
| `Production Technical System` → WildFly → Configuration → Interface → Inet Address | Inet address of the interface. |
| `Production Technical System` → WildFly → Configuration → Socket Binding Group → Port Offset | Port offset applied to bindings. |
| `Production Technical System` → WildFly → Configuration → Socket Binding → Port | Port number. |
| `Production Technical System` → WildFly → Configuration → Socket Binding → Interface Reference | Interface associated with the binding. |
| `Production Technical System` → WildFly → Configuration → Socket Binding → Fixed Port | Fixed-port flag. |
| `Production Technical System` → WildFly → Configuration → Outbound Socket Binding → Remote Host | Remote host. |
| `Production Technical System` → WildFly → Configuration → Outbound Socket Binding → Remote Port | Remote port. |
| `Production Technical System` → WildFly → Configuration → Outbound Socket Binding → Local Address | Local address used for outbound connections. |
| `Production Technical System` → WildFly → Configuration → System Property → Name | Property name. |
| `Production Technical System` → WildFly → Configuration → System Property → Value | Property value. |
| `Production Technical System` → WildFly → Configuration → System Property → Boot Time | Boot-time property flag. |
| `Production Technical System` → WildFly → Configuration → Environment Variable → Name | Environment variable name. |
| `Production Technical System` → WildFly → Configuration → Environment Variable → Value | Environment variable value. |
| `Production Technical System` → WildFly → Configuration → Path → Name | Path name. |
| `Production Technical System` → WildFly → Configuration → Path → Path Value | Absolute or relative path value. |
| `Production Technical System` → WildFly → Configuration → Descriptor-Driven Configuration | Constituting running server state from XML descriptors through DMR. |
| `Production Technical System` → WildFly → Server Architecture | Modular service-container architecture organizing subsystems, services, and deployments. |
| `Production Technical System` → WildFly → Server Architecture → Service Container Architecture | MSC-based runtime organizing services through dependencies and lifecycles. |
| `Production Technical System` → WildFly → Server Blueprints | Generative descriptions prescribing server construction, assembly, and deployment. |
| `Production Technical System` → WildFly → Server Blueprints → Source Tree | Versioned source prescribing server construction. |
| `Production Technical System` → WildFly → Server Blueprints → Feature-Pack Definitions | Galleon definitions prescribing installation composition. |
| `Production Technical System` → WildFly → Modularity | Decomposability into independently provisionable modules and layers. |
| `Production Technical System` → WildFly → Portability | Operability across operating systems and container runtimes. |
| `Production Technical System` → WildFly → Reliability | Degree of sustained correct service under expected conditions. |
| `Production Technical System` → WildFly → Maintainability | Degree to which the server can be patched, upgraded, and reconfigured. |
| `Production Technical System` → WildFly → Provisioning → Galleon → Feature Pack Repository | Repository of feature packs. |
| `Production Technical System` → WildFly → Provisioning → Galleon → Provisioning Plan | Plan describing features/layers to install. |
| `Production Technical System` → WildFly → Provisioning → Galleon → Provisioning Execution | Execution of the provisioning plan. |
| `Production Technical System` → WildFly → Provisioning → Feature → Feature Dependency | Dependency between features. |
| `Production Technical System` → WildFly → Provisioning → Feature → Feature Package | Package produced by a feature. |
| `Production Technical System` → WildFly → Provisioning → Layer → Layer Dependency | Dependency between layers. |
| `Production Technical System` → WildFly → Provisioning → Layer → Layer Feature | Feature contained in a layer. |
| `Production Technical System` → WildFly → Provisioning → Layer → Layer Package | Package contained in a layer. |
| `Production Technical System` → WildFly → Provisioning → WildFly Glow → Binary Scan | Scan of an application binary. |
| `Production Technical System` → WildFly → Provisioning → WildFly Glow → Feature Pack Discovery | Discovery of required feature packs. |
| `Production Technical System` → WildFly → Provisioning → WildFly Glow → Layer Discovery | Discovery of required layers. |
| `Production Technical System` → WildFly → Provisioning → Prospero → Install | Installation of a WildFly server. |
| `Production Technical System` → WildFly → Provisioning → Prospero → Update | Update of an installed WildFly server. |
| `Production Technical System` → WildFly → Provisioning → Prospero → Rollback | Rollback of an update. |
| `Production Technical System` → WildFly → Provisioning → Feature-Pack Assembly | Technique for composing server installations from feature packs and layers. |
| `Production Technical System` → WildFly → Provisioning → Layer Membership Criterion | Criterion distinguishing provisioned layers from non-members. |
| `Production Technical System` → WildFly → Provisioning → Layer Architecture | Shared Galleon feature-pack model integrating layers into one server. |
| `Production Technical System` → WildFly → Provisioning → Layer Provisioning Rules | Galleon provisioning rules governing layer composition. |
| `Production Technical System` → WildFly → Provisioning → Realized Runtime Capability | Jakarta EE runtime capability the layer composition collectively realizes. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.undertow` → Subsystem Registration | Registration of the Undertow subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.messaging-activemq` → Subsystem Registration | Registration of the ActiveMQ Artemis subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.elytron` → Subsystem Registration | Registration of the Elytron subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.io` → Subsystem Registration | Registration of the I/O subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.transactions` → Subsystem Registration | Registration of the transactions subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.batch.jberet` → Subsystem Registration | Registration of the Batch JBeret subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.health` → Subsystem Registration | Registration of the health subsystem. |
| `Production Technical System` → WildFly → Extensions → `org.wildfly.extension.metrics` → Subsystem Registration | Registration of the metrics subsystem. |
| `Production Technical System` → WildFly → Extensions → Extension Registration | Registering management resources and runtime services from extension modules. |
| `Production Technical System` → WildFly → Subsystems → EE → Default Bindings → Default Datasource Binding | Default datasource JNDI binding. |
| `Production Technical System` → WildFly → Subsystems → EE → Default Bindings → Default JMS Binding | Default JMS connection factory binding. |
| `Production Technical System` → WildFly → Subsystems → EE → Default Bindings → Default Concurrency Binding | Default concurrency utility binding. |
| `Production Technical System` → WildFly → Subsystems → EE → Global Modules → Module Reference | Reference to a globally visible module. |
| `Production Technical System` → WildFly → Subsystems → EE → Concurrency → Managed Executor | Managed executor service. |
| `Production Technical System` → WildFly → Subsystems → EE → Concurrency → Managed Scheduled Executor | Managed scheduled executor service. |
| `Production Technical System` → WildFly → Subsystems → EE → Concurrency → Managed Thread Factory | Managed thread factory. |
| `Production Technical System` → WildFly → Subsystems → EE → Concurrency → Context Service | Managed context propagation service. |
| `Production Technical System` → WildFly → Subsystems → EE → Managed Context Propagation | Propagating managed context to executors. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Bean Discovery → Archive Scanning | Scanning of deployment archives. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Bean Discovery → Bean Registration | Registration of discovered beans. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Dependency Injection → Injection Point Resolution | Resolution of injection points. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Dependency Injection → Instance Creation | Creation of injectable instances. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Interceptor → Binding | Interceptor binding. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Interceptor → Invocation | Interceptor invocation. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Decorator → Delegation | Decorator delegation. |
| `Production Technical System` → WildFly → Subsystems → CDI / Weld → Bean Discovery And Injection | Discovering beans and resolving injections. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateless Session Bean → Pooling | Pooling of stateless EJB instances. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateless Session Bean → Invocation | Invocation of stateless EJB methods. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateful Session Bean → Passivation | Passivation of stateful EJB state. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateful Session Bean → Activation | Activation of stateful EJB state. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Singleton Session Bean → Locking | Locking of singleton EJB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Singleton Session Bean → Startup | Startup of singleton EJB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Message-Driven Bean → Message Consumption | Consumption of messages by MDB. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Message-Driven Bean → Pooling | Pooling of MDB instances. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Container → Lifecycle Callbacks | Lifecycle callback invocations. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Container → Security Interceptors | Security interceptors. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Container → Transaction Interceptors | Transaction interceptors. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Pool → Pool Sizing | Pool size configuration. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → EJB Pool → Instance Creation | Creation of pooled EJB instances. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Remote Invocation → Serialization | Serialization of remote invocations. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Remote Invocation → Transport | Transport of remote invocations. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Timer Service → Timer Creation | Creation of EJB timers. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Timer Service → Timer Expiry | Expiry of EJB timers. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Timer Service → Timer Persistence | Persistence of EJB timers. |
| `Production Technical System` → WildFly → Subsystems → EJB3 → Stateful Passivation | Passivating and activating stateful bean state to and from storage. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Root Context | Root JNDI context. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Java: Context | java: namespace. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Java:comp Context | java:comp namespace. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Java:module Context | java:module namespace. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Java:app Context | java:app namespace. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Namespace → Java:global Context | java:global namespace. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Binding → Lookup | Lookup of bound resources. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Binding → Bind | Binding of resources. |
| `Production Technical System` → WildFly → Subsystems → Naming → JNDI Binding → Unbind | Unbinding of resources. |
| `Production Technical System` → WildFly → Subsystems → Naming → Remote Naming → Remote Lookup | Remote JNDI lookup. |
| `Production Technical System` → WildFly → Subsystems → Naming → Namespace Binding | Binding names to resources in namespaces. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → HTTP Listener | Default HTTP listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → AJP Listener | Default AJP listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → HTTPS Listener | Default HTTPS listener. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Host → Default Host → Virtual Host | Default virtual host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Host → Default Host → Access Log | Access log for the virtual host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Servlet Lifecycle | Servlet lifecycle management. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Session Management | HTTP session management. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Filter Chain | Servlet filter chain. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet → Init | Servlet initialization. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet → Service | Servlet request servicing. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet → Destroy | Servlet destruction. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Filter → Init | Filter initialization. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Filter → DoFilter | Filter chain execution. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Listener → Context Initialized | Context initialization callback. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Listener → Context Destroyed | Context destruction callback. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Handshake | WebSocket handshake. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Frame Handling | WebSocket frame handling. |
| `Production Technical System` → WildFly → Subsystems → Undertow → HTTP Invoker → EJB Invocation | HTTP-based EJB invocation. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Request Handling | Request handling by the handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Buffer Pool → Buffer Allocation | Allocation of buffers. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Buffer Pool → Buffer Release | Release of buffers. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Request Handling | Handling of REST requests. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Response Generation | Generation of REST responses. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Message Body Reader → Deserialization | Deserialization of request bodies. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Message Body Writer → Serialization | Serialization of response bodies. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Registration | Registration of providers. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Selection | Selection of providers for a request. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Jackson Provider → JSON Serialization | Jackson JSON serialization. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Jackson Provider → JSON Deserialization | Jackson JSON deserialization. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JSON-B Provider → JSON-B Serialization | JSON-B serialization. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JSON-P Provider → JSON-P Serialization | JSON-P serialization. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → JAXB Provider → XML Serialization | JAXB XML serialization. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Exception Mapper → Exception Mapping | Mapping of exceptions to responses. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Client → Request Build | Building of client requests. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Client → Response Handling | Handling of client responses. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Connection Acquisition | Acquisition of a database connection. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Connection Release | Release of a database connection. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA Start | XA transaction start. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA End | XA transaction end. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA Prepare | XA prepare phase. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA Commit | XA commit phase. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA Rollback | XA rollback phase. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Pool Sizing | Connection pool sizing. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Validation | Connection validation. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Eviction | Connection eviction. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JDBC Driver → Driver Loading | Loading of the JDBC driver. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JNDI Binding → Datasource Lookup | Lookup of the datasource via JNDI. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Recovery → Recovery Scan | Scan of in-doubt XA transactions. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Recovery → Recovery Commit | Recovery commit of XA transactions. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Security Domain → Credential Retrieval | Retrieval of datasource credentials. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation → Validation Query | Execution of the validation query. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Entity Manager Factory | Creation of the entity manager factory. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Entity Manager | Creation of entity managers. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Session Factory | Hibernate session factory. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Dialect Resolution | Resolution of the SQL dialect. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Persistence Context | Persistence context management. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Flush | Flush of persistence context. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → First-Level Cache | First-level (session) cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → Second-Level Cache | Second-level (shared) cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → Query Cache | Query result cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Cache Region | Cache region. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Cache Concurrency Strategy | Concurrency strategy for the cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Container → Default Cache | Default cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Container → Named Cache | Named cache. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Local Cache → Storage | Local cache storage. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache → Ownership | Ownership of cache entries. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache → Rebalancing | Rebalancing of cache entries. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Replicated Cache → Replication | Replication of cache entries. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Invalidation Cache → Invalidation | Invalidation of cache entries. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Persistent Cache → Cache Store | Persistent cache store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store → Write | Write to the cache store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store → Read | Read from the cache store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Eviction → Eviction Policy | Cache eviction policy. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Expiration → Lifespan | Cache entry lifespan. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Expiration → Max Idle | Cache entry max idle time. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → Send | Send on a JGroups channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → Receive | Receive on a JGroups channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Transport Protocol | Transport protocol in the stack. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Discovery Protocol | Discovery protocol in the stack. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Failure Detection Protocol | Failure detection protocol in the stack. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Ordering Protocol | Message ordering protocol. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Fragmentation Protocol | Message fragmentation protocol. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Flow Control Protocol | Flow control protocol. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport → TCP | TCP transport. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport → UDP | UDP transport. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Discovery Protocol → Multicast Discovery | Multicast-based discovery. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Failure Detection → Heartbeat | Heartbeat-based failure detection. |
| `Production Technical System` → WildFly → Subsystems → JGroups → MERGE3 → Merge Coordination | Coordination of cluster merges. |
| `Production Technical System` → WildFly → Subsystems → JGroups → FD_SOCK → Socket Monitoring | Socket-based monitoring for failures. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Node → Node Identity | Identity of the cluster node. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Node → Node State | State of the cluster node. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → Join | Join of a node to the cluster. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → Leave | Leave of a node from the cluster. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → View Change | Cluster view change. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Distributed Session Management → Session Replication | Replication of sessions. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Distributed Session Management → Session Failover | Failover of sessions. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Management → Session Creation | Creation of HTTP sessions. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Management → Session Invalidation | Invalidation of HTTP sessions. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Affinity → Node Affinity | Node affinity for sessions. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Replication → Replication Trigger | Trigger for session replication. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Replication → Replication Transport | Transport for session replication. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Service → Election | Election of the singleton provider. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Service → Failover | Failover of the singleton service. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Policy → Simple Policy | Simple singleton policy. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Policy → Random Policy | Random singleton policy. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Begin | Begin of a transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Commit | Commit of a transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Rollback | Rollback of a transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Suspend | Suspension of a transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Resume | Resumption of a transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction → Enlist Resource | Enlistment of a resource. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction → Delist Resource | Delisting of a resource. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → Prepare | Prepare phase of two-phase commit. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → Commit | Commit phase of two-phase commit. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → Rollback | Rollback phase of two-phase commit. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Manager | Transaction recovery manager. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Scan | Periodic recovery scan. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Transaction Log | Persistent transaction log. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Write | Write to the transaction log. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Read | Read from the transaction log. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout → Transaction Timeout | Transaction timeout value. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout → Reaper | Transaction reaper. |
| `Production Technical System` → WildFly → Subsystems → Transactions → JTS → ORB Integration | ORB integration for JTS. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Acceptors | Broker acceptors. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Connectors | Broker connectors. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Security Settings | Broker security settings. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Persistence | Message persistence. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Journal | Message journal. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Address Settings | Settings for the address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Bindings | Bindings of the address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Consumers | Queue consumers. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Messages | Queued messages. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Subscriptions | Topic subscriptions. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Messages | Topic messages. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Connection Creation | Creation of JMS connections. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Session Creation | Creation of JMS sessions. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connector → Transport | Transport of the connector. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Remote Connector → Remote Transport | Transport to the remote broker. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Acceptor → Transport | Transport of the acceptor. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory → Pooling | Pooling of JMS connections. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Source | Bridge source. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Target | Bridge target. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Quality Of Service | QoS of the bridge. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting → Authentication | Messaging authentication. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting → Authorization | Messaging authorization. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Dead Letter Address | Dead-letter address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Expiry Address | Expiry address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Max Size Bytes | Maximum address size. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Routing | Routing of diverted messages. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Deployment | Deployment of the resource adapter. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Connection Factory | Connection factory provided by the adapter. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Admin Object | Admin object provided by the adapter. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Managed Connection Factory | Managed connection factory. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Connection Factory Interface | Connection factory interface. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Connection Interface | Connection interface. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Admin Object → Admin Object Interface | Admin object interface. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Admin Object → Admin Object Properties | Admin object properties. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Activation → Activation Spec | Activation specification. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Activation → Message Listener | Message listener. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Authentication | Legacy authentication. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Authorization | Legacy authorization. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Mapping | Legacy role mapping. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Default Realm | Default realm of the domain. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Role Decoder | Role decoder. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Permission Mapper | Permission mapper. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm → Identity Acquisition | Acquisition of identities. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm → Credential Acquisition | Acquisition of credentials. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Identity Realm → Identity Store | Identity store. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Filesystem Realm → Filesystem Store | Filesystem-backed identity store. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JDBC Realm → SQL Query | SQL query for identity retrieval. |
| `Production Technical System` → WildFly → Subsystems → Elytron → LDAP Realm → LDAP Search | LDAP search for identities. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JAAS Realm → Login Context | JAAS login context. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Aggregate Realm → Realm Composition | Composition of multiple realms. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Caching Realm → Cache | Identity cache. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Key Entry | Key entry. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Certificate Entry | Certificate entry. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Trust Store → Trusted Certificate | Trusted certificate. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Credential Store → Credential Entry | Credential entry. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Authentication Factory → Mechanism Selection | Selection of authentication mechanism. |
| `Production Technical System` → WildFly → Subsystems → Elytron → HTTP Authentication Factory → HTTP Mechanism | HTTP authentication mechanism. |
| `Production Technical System` → WildFly → Subsystems → Elytron → SASL Authentication Factory → SASL Mechanism | SASL authentication mechanism. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Permission Mapper → Permission Assignment | Assignment of permissions. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Role Mapper → Role Transformation | Transformation of roles. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Principal Transformer → Principal Transformation | Transformation of principals. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Evidence Decoder → Evidence Decoding | Decoding of evidence. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Realm Mapper → Realm Mapping | Mapping across realms. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Protocol Selection | Selection of TLS protocol. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Cipher Suite Selection | Selection of cipher suites. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Certificate Revocation | Certificate revocation checking. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Cipher Suite → Cipher Name | Cipher suite name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Protocol → Protocol Name | TLS protocol name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Validation | Validation of OIDC tokens. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Refresh | Refresh of OIDC tokens. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Request Handling | Handling of SOAP requests. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Response Generation | Generation of SOAP responses. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Service Definition | Service definition in WSDL. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Binding Definition | Binding definition in WSDL. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Port Type Definition | Port-type definition in WSDL. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Message Definition | Message definition in WSDL. |
| `Production Technical System` → WildFly → Subsystems → Web Services → Handler Chain → Handler Invocation | Invocation of SOAP handlers. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Instance | Batch job instance. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Execution | Batch job execution. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Step Execution | Batch step execution. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Chunk Processing | Chunk processing. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Batchlet Processing | Batchlet processing. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Repository → Job State | Persistent job state. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Repository → Step State | Persistent step state. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Session Properties | Mail session properties. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Credentials | Mail session credentials. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Attribute | MBean attribute. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Operation | MBean operation. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Notification | MBean notification. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Server → Registration | MBean registration. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Server → Query | MBean query. |
| `Production Technical System` → WildFly → Subsystems → JMX → JMX Connector → Remote Access | Remote JMX access. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Level | Log level of the category. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Handlers | Handlers attached to the category. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Use Parent Handlers | Use-parent-handlers flag. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Level | Handler level. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Formatter | Handler formatter. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Filter | Handler filter. |
| `Production Technical System` → WildFly → Subsystems → Logging → File Handler → File Path | File path of the handler. |
| `Production Technical System` → WildFly → Subsystems → Logging → File Handler → Append | Append flag. |
| `Production Technical System` → WildFly → Subsystems → Logging → Console Handler → Target | Console target (stdout/stderr). |
| `Production Technical System` → WildFly → Subsystems → Logging → Periodic Rotating File Handler → Suffix | Rotation suffix pattern. |
| `Production Technical System` → WildFly → Subsystems → Logging → Size Rotating File Handler → Max File Size | Maximum file size. |
| `Production Technical System` → WildFly → Subsystems → Logging → Size Rotating File Handler → Max Backup Index | Maximum backup index. |
| `Production Technical System` → WildFly → Subsystems → Logging → Async Handler → Queue Length | Async queue length. |
| `Production Technical System` → WildFly → Subsystems → Logging → Async Handler → Overflow Action | Overflow action. |
| `Production Technical System` → WildFly → Subsystems → Logging → Formatter → Pattern | Format pattern. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Level → Severity | Severity threshold. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker → Task Queue | Worker task queue. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker → Thread Pool | Worker thread pool. |
| `Production Technical System` → WildFly → Subsystems → IO → Buffer Pool → Buffer Size | Buffer size. |
| `Production Technical System` → WildFly → Subsystems → IO → Buffer Pool → Buffer Count | Buffer count. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Connector → Transport | Transport of the connector. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Connector → Security | Security of the connector. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Endpoint → Listener | Listener of the endpoint. |
| `Production Technical System` → WildFly → Subsystems → Remoting → HTTP Upgrade → Upgrade Handshake | HTTP upgrade handshake. |
| `Production Technical System` → WildFly → Subsystems → Remoting → SASL Policy → Mechanism Selection | Selection of SASL mechanisms. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Discovery Provider → Static Provider | Static discovery provider. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Discovery Provider → Aggregate Provider | Aggregate discovery provider. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Static Discovery → Address List | Static address list. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Aggregate Discovery → Provider Composition | Composition of providers. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Proxy → Balancer | Balancer of the proxy. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Proxy → Node Registration | Node registration with the proxy. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise → Multicast | Multicast advertisement. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise → Socket Advertisement | Socket advertisement. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Balancer → Load Factor | Load factor. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Balancer → Sticky Session | Sticky-session configuration. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Node → Node Registration | Registration of the node. |
| `Production Technical System` → WildFly → Subsystems → Health → Health Check → UP | UP health result. |
| `Production Technical System` → WildFly → Subsystems → Health → Health Check → DOWN | DOWN health result. |
| `Production Technical System` → WildFly → Subsystems → Health → Readiness Check → READY | READY readiness result. |
| `Production Technical System` → WildFly → Subsystems → Health → Readiness Check → NOT_READY | NOT_READY readiness result. |
| `Production Technical System` → WildFly → Subsystems → Health → Liveness Check → ALIVE | ALIVE liveness result. |
| `Production Technical System` → WildFly → Subsystems → Health → Liveness Check → DEAD | DEAD liveness result. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Metric → Value | Metric value. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Metric → Unit | Metric unit. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Gauge → Reading | Gauge reading. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Counter → Increment | Counter increment. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Counter → Decrement | Counter decrement. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Histogram → Buckets | Histogram buckets. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Config → Property Source | Source of configuration properties. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Config → Property Value | Value of a configuration property. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Health → Health Check | Application health check. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Retry | Retry policy. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Timeout | Timeout policy. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Circuit Breaker | Circuit-breaker policy. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Bulkhead | Bulkhead policy. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Fallback | Fallback policy. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Reactive Messaging → Channel | Reactive messaging channel. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Reactive Messaging → Connector | Reactive messaging connector. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Metrics → Metric | Application metric. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI → Document | OpenAPI document. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI → Operation | OpenAPI operation. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Token | JWT token. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Claim | JWT claim. |
| `Production Technical System` → WildFly → Subsystems → SAR → SAR Deployment → Deployment | Deployment of a service archive. |
| `Production Technical System` → WildFly → Subsystems → SAR → SAR Deployment → Undeployment | Undeployment of a service archive. |
| `Production Technical System` → WildFly → Subsystems → SAR → MBean → Registration | Registration of the SAR MBean. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle | JSF lifecycle. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Component Tree | JSF component tree. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Renderer | JSF renderer. |
| `Production Technical System` → WildFly → Subsystems → JSF → `faces-config.xml` → Navigation Rules | JSF navigation rules. |
| `Production Technical System` → WildFly → Subsystems → JSF → `faces-config.xml` → Managed Beans | JSF managed beans. |
| `Production Technical System` → WildFly → Subsystems → POJO → POJO Deployment → Deployment | POJO deployment. |
| `Production Technical System` → WildFly → Subsystems → POJO → POJO Deployment → Undeployment | POJO undeployment. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Validator → Validation | Bean validation. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint → Definition | Constraint definition. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint → Violation | Constraint violation. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Scan | Scan of the deployment directory. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Deploy | Deployment of detected content. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Undeploy | Undeployment of removed content. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Scan Interval → Interval Value | Scan interval value. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Auto-Deploy → Enabled | Auto-deploy enabled flag. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Deployment Marker → Marker Type | Type of deployment marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Archive | Archive submitted for deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Descriptor | Descriptor of the deployment unit. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Structure | Structure of the deployment unit. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF | WEB-INF directory. |
| `Production Technical System` → WildFly → Deployment → WAR → META-INF | META-INF directory. |
| `Production Technical System` → WildFly → Deployment → WAR → Static Content | Static web content. |
| `Production Technical System` → WildFly → Deployment → WAR → Classes | Compiled classes. |
| `Production Technical System` → WildFly → Deployment → WAR → Libraries | Bundled libraries. |
| `Production Technical System` → WildFly → Deployment → JAR → META-INF | META-INF directory. |
| `Production Technical System` → WildFly → Deployment → JAR → Classes | Compiled classes. |
| `Production Technical System` → WildFly → Deployment → JAR → Resources | Packaged resources. |
| `Production Technical System` → WildFly → Deployment → EAR → Modules | Application modules. |
| `Production Technical System` → WildFly → Deployment → EAR → Libraries | Bundled libraries. |
| `Production Technical System` → WildFly → Deployment → EAR → META-INF | META-INF directory. |
| `Production Technical System` → WildFly → Deployment → RAR → META-INF | META-INF directory. |
| `Production Technical System` → WildFly → Deployment → RAR → Native Libraries | Native libraries. |
| `Production Technical System` → WildFly → Deployment → SAR → META-INF | META-INF directory. |
| `Production Technical System` → WildFly → Deployment → SAR → Service Classes | Service classes. |
| `Production Technical System` → WildFly → Deployment → Deployment Descriptor → Element | Declarative element in the descriptor. |
| `Production Technical System` → WildFly → Deployment → Deployment Descriptor → Schema Reference | Schema reference for the descriptor. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Servlet Declaration | Servlet declaration. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Filter Declaration | Filter declaration. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Listener Declaration | Listener declaration. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Welcome File | Welcome file declaration. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Security Constraint | Security constraint. |
| `Production Technical System` → WildFly → Deployment → `jboss-web.xml` → Context Root | Context root. |
| `Production Technical System` → WildFly → Deployment → `jboss-web.xml` → Virtual Host | Virtual host. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Session Bean | Session bean declaration. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Message-Driven Bean | Message-driven bean declaration. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Assembly Descriptor | Assembly descriptor. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Persistence Unit | Persistence unit declaration. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Class List | List of persistence classes. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Properties | Persistence properties. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Discovery Mode | Bean discovery mode. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Interceptors | Interceptor declarations. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Decorators | Decorator declarations. |
| `Production Technical System` → WildFly → Deployment → `application.xml` → Module | Application module declaration. |
| `Production Technical System` → WildFly → Deployment → `application.xml` → Security Role | Security role declaration. |
| `Production Technical System` → WildFly → Deployment → `jboss-app.xml` → Class Loading | Class-loading configuration. |
| `Production Technical System` → WildFly → Deployment → `ra.xml` → Resource Adapter | Resource-adapter declaration. |
| `Production Technical System` → WildFly → Deployment → `ra.xml` → Connection Definition | Connection-definition declaration. |
| `Production Technical System` → WildFly → Deployment → `ironjacamar.xml` → Connection Pool | Connection-pool configuration. |
| `Production Technical System` → WildFly → Deployment → `application-client.xml` → Client Descriptor | Client descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-client.xml` → Client Descriptor | JBoss client descriptor. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Dependencies | Deployment dependencies. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Exclusions | Deployment exclusions. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Local Resources | Local resource declarations. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Class Annotation | Class-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Method Annotation | Method-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Field Annotation | Field-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Parse | Parse phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Register | Register phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Deploy | Deploy phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → STRUCTURE | STRUCTURE phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → PARSE | PARSE phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → REGISTER | REGISTER phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → DEPENDENCIES | DEPENDENCIES phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → CONFIGURE_MODULE | CONFIGURE_MODULE phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → POST_MODULE | POST_MODULE phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → INSTALL | INSTALL phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → CLEANUP | CLEANUP phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit Processor → Transform | Transformation of deployment state. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Registration | Registration of the deployment service. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Start | Start of the deployment service. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Stop | Stop of the deployment service. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Deploy | Deploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Undeploy | Undeploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Redeploy | Redeploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Replace | Replace transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Explode | Explode transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Scan | Scan of the deployment directory. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Deploy | Deployment of detected content. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Undeploy | Undeployment of removed content. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.dodeploy` | Marker for deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.undeploy` | Marker for undeployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.deployed` | Marker for successful deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.failed` | Marker for failed deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.isdeploying` | Marker for in-progress deployment. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.skipdeploy` | Marker for skipped deployment. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Classes | Application module classes. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Resources | Application module resources. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Libraries | Application module libraries. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Class Loader | Application module class loader. |
| `Production Technical System` → WildFly → Deployment → Application → Component → Servlet Component | Servlet component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → EJB Component | EJB component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → CDI Component | CDI component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → REST Component | REST component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → WebSocket Component | WebSocket component. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Lifecycle | Servlet lifecycle. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Request Handling | Servlet request handling. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Session Handling | Servlet session handling. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Scope | CDI bean scope. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Lifecycle | CDI bean lifecycle. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Injection | CDI bean injection. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle | EJB lifecycle. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Business Interface | EJB business interface. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Transaction Attribute | EJB transaction attribute. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Security Role | EJB security role. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Resource Method | REST resource method. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Path | REST resource path. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Media Type | REST media type. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Entity | JPA entity. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Entity Manager Factory | Entity manager factory. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Data Source | Data source reference. |
| `Production Technical System` → WildFly → Deployment → Application → JNDI Resource → Resource Reference | Resource reference. |
| `Production Technical System` → WildFly → Deployment → Application → JNDI Resource → Environment Entry | Environment entry. |
| `Production Technical System` → WildFly → Deployment → Application → Security Domain Association → Domain Reference | Reference to the security domain. |
| `Production Technical System` → WildFly → Deployment → Application → Datasource Dependency → Datasource Reference | Reference to the datasource. |
| `Production Technical System` → WildFly → Deployment → Application → Messaging Dependency → Connection Factory Reference | Reference to the connection factory. |
| `Production Technical System` → WildFly → Deployment → Application → Messaging Dependency → Destination Reference | Reference to the destination. |
| `Production Technical System` → WildFly → Deployment → Application → Module Dependency → Module Reference | Reference to a WildFly module. |
| `Production Technical System` → WildFly → Deployment → Application → Module Dependency → Export | Export of module packages. |
| `Production Technical System` → WildFly → Network → Public Interface → Inet Address | Public interface inet address. |
| `Production Technical System` → WildFly → Network → Management Interface → Inet Address | Management interface inet address. |
| `Production Technical System` → WildFly → Network → Unsecure Interface → Inet Address | Unsecure interface inet address. |
| `Production Technical System` → WildFly → Network → HTTP Endpoint → Port | HTTP port. |
| `Production Technical System` → WildFly → Network → HTTPS Endpoint → Port | HTTPS port. |
| `Production Technical System` → WildFly → Network → HTTPS Endpoint → Certificate | TLS certificate. |
| `Production Technical System` → WildFly → Network → AJP Endpoint → Port | AJP port. |
| `Production Technical System` → WildFly → Network → Remoting Endpoint → Port | Remoting port. |
| `Production Technical System` → WildFly → Network → Messaging Endpoint → Port | Messaging port. |
| `Production Technical System` → WildFly → Network → JGroups Endpoint → Port | JGroups port. |
| `Production Technical System` → WildFly → Network → TXN Recovery Endpoint → Port | TXN recovery port. |
| `Production Technical System` → WildFly → Network → TXN Status Manager Endpoint → Port | TXN status manager port. |
| `Production Technical System` → WildFly → Network → Management HTTP Endpoint → Port | Management HTTP port (9990). |
| `Production Technical System` → WildFly → Network → Management Native Endpoint → Port | Management native port (9999). |
| `Production Technical System` → WildFly → Network → Socket Binding → Name | Socket binding name. |
| `Production Technical System` → WildFly → Network → Socket Binding → Port | Socket binding port. |
| `Production Technical System` → WildFly → Network → Socket Binding → Interface | Socket binding interface. |
| `Production Technical System` → WildFly → Network → Socket Binding Group → Default Interface | Default interface of the group. |
| `Production Technical System` → WildFly → Network → Socket Binding Group → Port Offset | Port offset of the group. |
| `Production Technical System` → WildFly → Network → Port Offset → Offset Value | Port offset value. |
| `Production Technical System` → WildFly → Network → Outbound Socket Binding → Remote Host | Remote host. |
| `Production Technical System` → WildFly → Network → Outbound Socket Binding → Remote Port | Remote port. |
| `Production Technical System` → WildFly → Runtime Security → Authentication → Mechanism | Authentication mechanism. |
| `Production Technical System` → WildFly → Runtime Security → Authentication → Credential | Credential used for authentication. |
| `Production Technical System` → WildFly → Runtime Security → Authorization → Policy | Authorization policy. |
| `Production Technical System` → WildFly → Runtime Security → Authorization → Decision | Authorization decision. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Handshake | TLS handshake. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Cipher Negotiation | Cipher negotiation. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Certificate Validation | Certificate validation. |
| `Production Technical System` → WildFly → Runtime Security → Credential Store → Entry | Credential entry. |
| `Production Technical System` → WildFly → Runtime Security → Credential Store → Alias | Credential alias. |
| `Production Technical System` → WildFly → Runtime Security → Identity → Name | Identity name. |
| `Production Technical System` → WildFly → Runtime Security → Identity → Attributes | Identity attributes. |
| `Production Technical System` → WildFly → Runtime Security → Principal → Name | Principal name. |
| `Production Technical System` → WildFly → Runtime Security → Role → Name | Role name. |
| `Production Technical System` → WildFly → Runtime Security → Permission → Name | Permission name. |
| `Production Technical System` → WildFly → Runtime Security → Permission → Actions | Permission actions. |
| `Production Technical System` → WildFly → Runtime Security → Security Event → Type | Type of security event. |
| `Production Technical System` → WildFly → Runtime Security → Security Event → Timestamp | Timestamp of the event. |
| `Production Technical System` → WildFly → Runtime Security → Audit Event → Category | Category of audit event. |
| `Production Technical System` → WildFly → Runtime Security → Audit Event → Outcome | Outcome of the audited event. |
| `Production Technical System` → WildFly → Runtime Security → Security Domain → Name | Security domain name. |
| `Production Technical System` → WildFly → Runtime Security → Security Domain → Realm | Realm of the security domain. |
| `Production Technical System` → WildFly → Runtime Security → Realm → Name | Realm name. |
| `Production Technical System` → WildFly → Runtime Security → Realm → Identity Store | Identity store of the realm. |
| `Production Technical System` → WildFly → Runtime Security → SSL Context → Protocol | TLS protocol of the context. |
| `Production Technical System` → WildFly → Runtime Security → SSL Context → Cipher Suites | Cipher suites of the context. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Active Profile | Active configuration profile. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Running Mode | Running mode (standalone/domain). |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Server State | Server state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Started | Started state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Stopped | Stopped state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Reload Required | Reload-required state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Restart Required | Restart-required state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Name | Metric name. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Value | Metric value. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Unit | Metric unit. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Level | Log event level. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Message | Log event message. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Timestamp | Log event timestamp. |
| `Production Technical System` → WildFly → Runtime Control → Health Result → Status | Health status. |
| `Production Technical System` → WildFly → Runtime Control → Health Result → Check | Health check name. |
| `Production Technical System` → WildFly → Runtime Control → Diagnostic Report → Section | Diagnostic report section. |
| `Production Technical System` → WildFly → Runtime Control → JDR → Collection | Diagnostic data collection. |
| `Production Technical System` → WildFly → Runtime Control → JDR → Report | Diagnostic report generation. |
| `Production Technical System` → WildFly → Runtime Control → Audit Log → Entry | Audit log entry. |
| `Production Technical System` → WildFly → Runtime Control → Server Log → Entry | Server log entry. |
| `Production Technical System` → WildFly → Runtime Control → GC Log → Entry | GC log entry. |
| `Production Technical System` → WildFly → Runtime Control → Thread Dump → Thread | Thread in the dump. |
| `Production Technical System` → WildFly → Runtime Control → Heap Dump → Heap Region | Heap region in the dump. |
| `Production Technical System` → WildFly → Lifecycle → Provision → Provisioning Plan | Plan for provisioning. |
| `Production Technical System` → WildFly → Lifecycle → Provision → Provisioning Execution | Execution of provisioning. |
| `Production Technical System` → WildFly → Lifecycle → Install → Distribution Extraction | Extraction of the distribution. |
| `Production Technical System` → WildFly → Lifecycle → Install → File Placement | Placement of installation files. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Profile Selection | Selection of the configuration profile. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Subsystem Configuration | Configuration of subsystems. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Interface Configuration | Configuration of network interfaces. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Socket Binding Configuration | Configuration of socket bindings. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Security Configuration | Configuration of security domains. |
| `Production Technical System` → WildFly → Lifecycle → Start → Service Container Start | Start of the service container. |
| `Production Technical System` → WildFly → Lifecycle → Start → Subsystem Start | Start of subsystems. |
| `Production Technical System` → WildFly → Lifecycle → Start → Deployment Start | Start of deployments. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Bootstrap | Bootstrap phase. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Configuration Load | Loading of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Service Installation | Installation of services. |
| `Production Technical System` → WildFly → Lifecycle → Deploy → Deployment Processing | Processing of the deployment. |
| `Production Technical System` → WildFly → Lifecycle → Deploy → Deployment Start | Start of the deployed application. |
| `Production Technical System` → WildFly → Lifecycle → Redeploy → Undeploy | Undeploy phase of redeploy. |
| `Production Technical System` → WildFly → Lifecycle → Redeploy → Deploy | Deploy phase of redeploy. |
| `Production Technical System` → WildFly → Lifecycle → Reload → Stop | Stop phase of reload. |
| `Production Technical System` → WildFly → Lifecycle → Reload → Start | Start phase of reload. |
| `Production Technical System` → WildFly → Lifecycle → Shutdown → Graceful Shutdown | Graceful shutdown. |
| `Production Technical System` → WildFly → Lifecycle → Shutdown → Forced Shutdown | Forced shutdown. |
| `Production Technical System` → WildFly → Lifecycle → Undeploy → Deployment Stop | Stop of the deployed application. |
| `Production Technical System` → WildFly → Lifecycle → Undeploy → Content Removal | Removal of deployment content. |
| `Production Technical System` → WildFly → Lifecycle → Maintain → Corrective Maintenance | Corrective maintenance. |
| `Production Technical System` → WildFly → Lifecycle → Maintain → Preventive Maintenance | Preventive maintenance. |
| `Production Technical System` → WildFly → Lifecycle → Patch → Patch Application | Application of the patch. |
| `Production Technical System` → WildFly → Lifecycle → Patch → Patch Verification | Verification of the patch. |
| `Production Technical System` → WildFly → Lifecycle → Upgrade → Version Change | Change to a new version. |
| `Production Technical System` → WildFly → Lifecycle → Upgrade → Configuration Migration | Migration of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Migrate → Configuration Transformation | Transformation of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Migrate → Application Migration | Migration of applications. |
| `Production Technical System` → WildFly → Lifecycle → Retire → Decommissioning | Decommissioning of the server. |
| `Production Technical System` → WildFly → Lifecycle → Retire → Data Archival | Archival of data. |
| `Production Technical System` → WildFly → Lifecycle → Rollback → Version Reversion | Reversion to a previous version. |
| `Production Technical System` → WildFly → Lifecycle → Rollback → Configuration Reversion | Reversion of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Configuration Backup | Backup of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Data Backup | Backup of data. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Deployment Backup | Backup of deployments. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Configuration Restore | Restore of configuration. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Data Restore | Restore of data. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Deployment Restore | Restore of deployments. |
| `Production Technical System` → WildFly → External Resources → CPU → Core | CPU core. |
| `Production Technical System` → WildFly → External Resources → CPU → Frequency | CPU frequency. |
| `Production Technical System` → WildFly → External Resources → Memory → Heap | Runtime heap. |
| `Production Technical System` → WildFly → External Resources → Memory → Off-Heap | Off-heap memory. |
| `Production Technical System` → WildFly → External Resources → Filesystem → Disk | Disk storage. |
| `Production Technical System` → WildFly → External Resources → Filesystem → Files | Files accessed by the runtime. |
| `Production Technical System` → WildFly → External Resources → Network → Bandwidth | Network bandwidth. |
| `Production Technical System` → WildFly → External Resources → Network → Latency | Network latency. |
| `Production Technical System` → WildFly → External Resources → Database → Connection | Database connection. |
| `Production Technical System` → WildFly → External Resources → Database → Storage | Database storage. |
| `Production Technical System` → WildFly → External Resources → Message Broker → Queue | Broker queue. |
| `Production Technical System` → WildFly → External Resources → Message Broker → Topic | Broker topic. |
| `Production Technical System` → WildFly → External Resources → Identity Provider → Realm | Identity provider realm. |
| `Production Technical System` → WildFly → External Resources → Identity Provider → Endpoint | Identity provider endpoint. |
| `Production Technical System` → WildFly → External Resources → Certificate Authority → Root Certificate | Root certificate. |
| `Production Technical System` → WildFly → External Resources → Certificate Authority → CRL | Certificate revocation list. |
| `Production Technical System` → WildFly → External Resources → Load Balancer → Virtual IP | Virtual IP of the load balancer. |
| `Production Technical System` → WildFly → External Resources → Load Balancer → Pool | Backend pool. |
| `Production Technical System` → WildFly → External Resources → JDK → JRE | Java runtime. |
| `Production Technical System` → WildFly → External Resources → JDK → JDK Tools | JDK tools. |
| `Production Technical System` → WildFly → External Resources → Operating System → Kernel | OS kernel. |
| `Production Technical System` → WildFly → External Resources → Operating System → Libraries | OS libraries. |
| `Production Technical System` → WildFly → External Resources → Container Runtime → Image | Container image. |
| `Production Technical System` → WildFly → External Resources → Container Runtime → Volume | Container volume. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Namespace | Kubernetes namespace. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Service | Kubernetes service. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → ConfigMap | Kubernetes ConfigMap. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Secret | Kubernetes Secret. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Ingress | Kubernetes Ingress. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta EE → Profile | Jakarta EE profile. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Servlet → Version | Jakarta Servlet version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta REST → Version | Jakarta REST version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Enterprise Beans → Version | Jakarta EJB version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Persistence → Version | Jakarta Persistence version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Messaging → Version | Jakarta Messaging version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta CDI → Version | Jakarta CDI version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Transactions → Version | Jakarta Transactions version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Bean Validation → Version | Jakarta Bean Validation version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Batch → Version | Jakarta Batch version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Concurrency → Version | Jakarta Concurrency version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Connectors → Version | Jakarta Connectors version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Mail → Version | Jakarta Mail version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta WebSocket → Version | Jakarta WebSocket version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Binding → Version | Jakarta JSON-B version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Processing → Version | Jakarta JSON-P version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Binding → Version | Jakarta XML Binding version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Web Services → Version | Jakarta XML WS version. |
| `Production Technical System` → WildFly → Technical Standards → JDBC → Version | JDBC version. |
| `Production Technical System` → WildFly → Technical Standards → JNDI → Version | JNDI version. |
| `Production Technical System` → WildFly → Technical Standards → JMX → Version | JMX version. |
| `Production Technical System` → WildFly → Technical Standards → HTTP → Version | HTTP version. |
| `Production Technical System` → WildFly → Technical Standards → HTTPS → Version | HTTPS version. |
| `Production Technical System` → WildFly → Technical Standards → TLS → Version | TLS version. |
| `Production Technical System` → WildFly → Technical Standards → AJP → Version | AJP version. |
| `Production Technical System` → WildFly → Technical Standards → WebSocket → Version | WebSocket version. |
| `Production Technical System` → WildFly → Technical Standards → OIDC → Version | OIDC version. |
| `Production Technical System` → WildFly → Technical Standards → OAuth 2.0 → Version | OAuth 2.0 version. |
| `Production Technical System` → WildFly → Technical Standards → SAML → Version | SAML version. |
| `Production Technical System` → WildFly → Technical Standards → JWT → Version | JWT version. |
| `Production Technical System` → WildFly → Technical Standards → MicroProfile → Version | MicroProfile version. |
| `Production Technical System` → WildFly → Technical Standards → OpenAPI → Version | OpenAPI version. |
| `Production Technical System` → WildFly → Technical Standards → OpenTelemetry → Version | OpenTelemetry version. |
| `Production Technical System` → WildFly → Technical Practices → Provisioning → Plan Definition | Definition of the provisioning plan. |
| `Production Technical System` → WildFly → Technical Practices → Provisioning → Execution | Execution of provisioning. |
| `Production Technical System` → WildFly → Technical Practices → Configuration Management → Change Control | Control of configuration changes. |
| `Production Technical System` → WildFly → Technical Practices → Configuration Management → Version Control | Versioning of configuration. |
| `Production Technical System` → WildFly → Technical Practices → Application Deployment → Release Process | Process of releasing applications. |
| `Production Technical System` → WildFly → Technical Practices → Application Deployment → Rollback Process | Process of rolling back applications. |
| `Production Technical System` → WildFly → Technical Practices → Monitoring → Metric Collection | Collection of runtime metrics. |
| `Production Technical System` → WildFly → Technical Practices → Monitoring → Alerting | Alerting on monitored conditions. |
| `Production Technical System` → WildFly → Technical Practices → Health Checking → Probe Scheduling | Scheduling of health probes. |
| `Production Technical System` → WildFly → Technical Practices → Health Checking → Result Handling | Handling of health-check results. |
| `Production Technical System` → WildFly → Technical Practices → Log Analysis → Collection | Collection of log events. |
| `Production Technical System` → WildFly → Technical Practices → Log Analysis → Interpretation | Interpretation of log events. |
| `Production Technical System` → WildFly → Technical Practices → Backup / Recovery → Backup Scheduling | Scheduling of backups. |
| `Production Technical System` → WildFly → Technical Practices → Backup / Recovery → Restore Procedure | Procedure for restore. |
| `Production Technical System` → WildFly → Technical Practices → Patching → Patch Planning | Planning of patches. |
| `Production Technical System` → WildFly → Technical Practices → Patching → Patch Application | Application of patches. |
| `Production Technical System` → WildFly → Technical Practices → Capacity Management → Sizing | Capacity sizing. |
| `Production Technical System` → WildFly → Technical Practices → Capacity Management → Scaling | Capacity scaling. |
| `Production Technical System` → WildFly → Technical Practices → Security Hardening → Exposure Reduction | Reduction of exposure. |
| `Production Technical System` → WildFly → Technical Practices → Security Hardening → Configuration Hardening | Hardening of configuration. |
| `Production Technical System` → WildFly → Technical Practices → Performance Tuning → JVM Tuning | Tuning of the JVM. |
| `Production Technical System` → WildFly → Technical Practices → Performance Tuning → Subsystem Tuning | Tuning of subsystems. |
| `Production Technical System` → WildFly → Technical Practices → Thread Management → Pool Sizing | Sizing of thread pools. |
| `Production Technical System` → WildFly → Technical Practices → Thread Management → Queue Sizing | Sizing of thread queues. |
| `Production Technical System` → WildFly → Technical Practices → Connection Pool Tuning → Pool Sizing | Sizing of connection pools. |
| `Production Technical System` → WildFly → Technical Practices → Connection Pool Tuning → Timeout Tuning | Tuning of connection timeouts. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → Heap Sizing | Sizing of the JVM heap. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → GC Selection | Selection of the garbage collector. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → System Property Tuning | Tuning of system properties. |
| `Production Technical System` → WildFly → Technical Dependencies → JVM → Java Version | Required Java version. |
| `Production Technical System` → WildFly → Technical Dependencies → JVM → JVM Options | Required JVM options. |
| `Production Technical System` → WildFly → Technical Dependencies → Operating System → OS Family | Required OS family. |
| `Production Technical System` → WildFly → Technical Dependencies → Operating System → OS Libraries | Required OS libraries. |
| `Production Technical System` → WildFly → Technical Dependencies → Filesystem → Paths | Required filesystem paths. |
| `Production Technical System` → WildFly → Technical Dependencies → Filesystem → Permissions | Required filesystem permissions. |
| `Production Technical System` → WildFly → Technical Dependencies → Network Stack → Protocols | Required network protocols. |
| `Production Technical System` → WildFly → Technical Dependencies → Network Stack → Ports | Required network ports. |
| `Production Technical System` → WildFly → Technical Dependencies → Database → JDBC Driver | Required JDBC driver. |
| `Production Technical System` → WildFly → Technical Dependencies → Database → Schema | Required database schema. |
| `Production Technical System` → WildFly → Technical Dependencies → External Services → Endpoint | Required external endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → External Services → Credentials | Required external credentials. |
| `Production Technical System` → WildFly → Technical Dependencies → Message Broker → Broker Endpoint | Required broker endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → Message Broker → Destinations | Required destinations. |
| `Production Technical System` → WildFly → Technical Dependencies → Identity Provider → IdP Endpoint | Required IdP endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → Identity Provider → Client Credentials | Required client credentials. |
| `Production Technical System` → WildFly → Technical Dependencies → Certificate Authority → Root Certificate | Required root certificate. |
| `Production Technical System` → WildFly → Technical Dependencies → Certificate Authority → Trust Chain | Required trust chain. |
| `Production Technical System` → WildFly → Technical Dependencies → Load Balancer → Frontend Address | Required frontend address. |
| `Production Technical System` → WildFly → Technical Dependencies → Load Balancer → Backend Pool | Required backend pool. |
| `Production Technical System` → WildFly → Technical Dependencies → Container Runtime → Image | Required container image. |
| `Production Technical System` → WildFly → Technical Dependencies → Container Runtime → Volume | Required container volume. |
| `Production Technical System` → WildFly → Technical Dependencies → Kubernetes API → API Server | Required API server. |
| `Production Technical System` → WildFly → Technical Dependencies → Kubernetes API → Service Account | Required service account. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Unit Test | Unit test execution. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Integration Test | Integration test execution. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Static Analysis | Static analysis. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Inspection | Dimensional inspection. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → User Validation | User validation. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → Operational Trial | Operational trial. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → Acceptance Test | Acceptance test. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Log Feedback | Log-based feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Metric Feedback | Metric-based feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Health Feedback | Health-based feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Management State Feedback | Management-state feedback. |
| `Production Technical System` → WildFly → Technical Control → Failure → Crash | Crash failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Hang | Hang failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Deadlock | Deadlock failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Memory Leak | Memory-leak failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Thread Leak | Thread-leak failure. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Exposed Voltage | Exposed-voltage hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Thermal Runaway | Thermal-runaway hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Race Condition | Race-condition hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Resource Exhaustion | Resource-exhaustion hazard. |
| `Production Technical System` → WildFly → Technical Control → Risk → Availability Risk | Availability risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Integrity Risk | Integrity risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Confidentiality Risk | Confidentiality risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Compliance Risk | Compliance risk. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Performance Vs Energy | Performance-vs-energy trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Flexibility Vs Complexity | Flexibility-vs-complexity trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Availability Vs Consistency | Availability-vs-consistency trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Security Vs Usability | Security-vs-usability trade-off. |
| `Production Technical System` → WildFly → Technical Control → Performance → Response Time | Response-time measurement. |
| `Production Technical System` → WildFly → Technical Control → Performance → Throughput | Throughput measurement. |
| `Production Technical System` → WildFly → Technical Control → Performance → Resource Consumption | Resource-consumption measurement. |
| `Production Technical System` → WildFly → Technical Control → Availability → Uptime | Uptime measurement. |
| `Production Technical System` → WildFly → Technical Control → Availability → Downtime | Downtime measurement. |
| `Production Technical System` → WildFly → Technical Control → Throughput → Requests Per Second | Requests-per-second metric. |
| `Production Technical System` → WildFly → Technical Control → Throughput → Bytes Per Second | Bytes-per-second metric. |
| `Production Technical System` → WildFly → Technical Control → Latency → P50 | Median latency. |
| `Production Technical System` → WildFly → Technical Control → Latency → P95 | 95th-percentile latency. |
| `Production Technical System` → WildFly → Technical Control → Latency → P99 | 99th-percentile latency. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → CPU Utilization | CPU-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Memory Utilization | Memory-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Disk Utilization | Disk-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Network Utilization | Network-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → HTTP 5xx Rate | HTTP 5xx error rate. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → Exception Rate | Exception rate. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → Timeout Rate | Timeout rate. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Thread Pool Saturation | Thread-pool saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Connection Pool Saturation | Connection-pool saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Heap Saturation | Heap saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Queue Saturation | Queue saturation. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Listener | Endpoint listeners of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Listener → HTTP Listener | HTTP listener of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Listener → HTTPS Listener | HTTPS listener of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Listener → AJP Listener | AJP listener of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host | Virtual-host resources of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host → Default Host | Default host of the default server. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host → Default Host → Location | Filesystem location served by the host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host → Default Host → Access Log | Access log of the default host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host → Default Host → Filter | HTTP filter of the default host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Server → Default Server → Host → Default Host → Handler | Request handler of the default host. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Deployment | Deployment of a web application. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Servlet Context | Servlet context. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Session Manager | HTTP session manager. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Session Cookie | Session cookie configuration. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Session Timeout | Session timeout. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Welcome File | Welcome file handling. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → MIME Mapping | MIME-type mapping. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Error Page | Error-page mapping. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Security Constraint | Security constraint enforcement. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Servlet Mapping | Servlet URL mapping. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Filter Mapping | Filter URL mapping. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Servlet Container → Listener Registration | Listener registration. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Endpoint | WebSocket endpoint. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Session | WebSocket session. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Message Encoder | WebSocket message encoder. |
| `Production Technical System` → WildFly → Subsystems → Undertow → WebSocket → Message Decoder | WebSocket message decoder. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → File Handler | Static file handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Directory Handler | Directory listing handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Resource Handler | Classpath resource handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Redirect Handler | Redirect handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Proxy Handler | Reverse proxy handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Access Log Handler | Access log handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Graceful Shutdown Handler | Graceful shutdown handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Request Limiting Handler | Request limiting handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Blocking Handler | Blocking handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Compression Handler | Compression handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Byte-Range Handler | Byte-range handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Handler → Path Template Handler | Path-template handler. |
| `Production Technical System` → WildFly → Subsystems → Undertow → Request Handling | Handling requests through the server, host, and servlet chain. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Path Template | REST path template. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → HTTP Method | HTTP method binding. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Consumes | Consumed media types. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Produces | Produced media types. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Parameter Binding | REST parameter binding. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Request Context | REST request context. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Response Builder | REST response builder. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → REST Endpoint → Exception Mapping | REST exception mapping. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Filter | REST filter provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Interceptor | REST interceptor provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Context Resolver | REST context resolver. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Param Converter | REST parameter converter. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Feature | REST feature provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Provider → Dynamic Feature | REST dynamic feature provider. |
| `Production Technical System` → WildFly → Subsystems → RESTEasy → Message Body Processing | Deserializing requests and serializing responses through providers. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Connection URL | JDBC connection URL. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → User Name | Datasource user name. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Password | Datasource password. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Driver Class | JDBC driver class. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Transaction Isolation | Transaction isolation level. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Pool Configuration | Connection-pool configuration. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Validation Configuration | Connection-validation configuration. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Timeout Configuration | Connection-timeout configuration. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Datasource → Statement Cache | Statement cache. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → XA Properties | XA properties. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → Recovery Credentials | XA recovery credentials. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → Recovery Username | XA recovery username. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Datasource → Recovery Password | XA recovery password. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Initial Size | Initial pool size. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Minimum Size | Minimum pool size. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Maximum Size | Maximum pool size. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Idle Timeout | Idle timeout. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Leak Detection | Leak detection. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pool → Flush Strategy | Pool flush strategy. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JDBC Driver → Module Name | JDBC driver module name. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JDBC Driver → Class Name | JDBC driver class name. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JDBC Driver → XA Datasource Class | XA datasource class. |
| `Production Technical System` → WildFly → Subsystems → Datasources → JNDI Binding → Binding Name | JNDI binding name. |
| `Production Technical System` → WildFly → Subsystems → Datasources → XA Recovery → Recovery Module | XA recovery module. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Security Domain → Domain Name | Security domain name. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation → Check Valid Connection SQL | Validation SQL. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation → Validate On Match | Validate-on-match flag. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation → Background Validation | Background-validation flag. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Validation → Background Validation Millis | Background-validation interval. |
| `Production Technical System` → WildFly → Subsystems → Datasources → Connection Pooling | Sharing managed database connections from a pool. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Name | Persistence unit name. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Transaction Type | Persistence-unit transaction type. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Provider | Persistence provider. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Data Source | Persistence-unit datasource. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Managed Classes | Managed persistence classes. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Mapping File | ORM mapping file. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Unit → Properties | Persistence-unit properties. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Dialect | Hibernate SQL dialect. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → JDBC Bind | JDBC parameter binding. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Statement Preparation | SQL statement preparation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Result Set Handling | Result-set handling. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Entity Persister | Entity persister. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Collection Persister | Collection persister. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Identifier Generator | Identifier generator. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Dirty Checking | Dirty checking. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate ORM → Flush Mode | Flush mode. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Persist | Entity persist operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Merge | Entity merge operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Remove | Entity remove operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Find | Entity find operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Query | Query execution. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Lock | Entity lock operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Entity Manager → Refresh | Entity refresh operation. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → Cache Region Factory | Cache region factory. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → Cache Provider | Cache provider. |
| `Production Technical System` → WildFly → Subsystems → JPA → Hibernate Cache → Cache Concurrency Strategy | Cache concurrency strategy. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Entity Cache | Entity-level cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Collection Cache | Collection-level cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Natural Id Cache | Natural-id cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Query Cache | Query-level cache. |
| `Production Technical System` → WildFly → Subsystems → JPA → Second-Level Cache → Cache Eviction | Cache eviction. |
| `Production Technical System` → WildFly → Subsystems → JPA → Persistence Context Management | Managing entity state within persistence contexts. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Container → Transport | Cache-container transport. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Container → Global Configuration | Global cache configuration. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Local Cache → Mode | Local cache mode. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache → Owners | Number of owners. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache → Segments | Number of segments. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Cache → L1 Lifespan | L1 cache lifespan. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Replicated Cache → Sync Replication | Synchronous replication. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Replicated Cache → Async Replication | Asynchronous replication. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Invalidation Cache → Invalidation Threshold | Invalidation threshold. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Persistent Cache → Store Type | Cache-store type. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store → Write Behind | Write-behind store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store → Write Through | Write-through store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Cache Store → Read Through | Read-through store. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Eviction → Eviction Strategy | Eviction strategy. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Eviction → Eviction Max Entries | Maximum entries before eviction. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Expiration → Interval | Expiration interval. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Expiration → Reaper | Expiration reaper. |
| `Production Technical System` → WildFly → Subsystems → Infinispan → Distributed Caching | Storing and retrieving entries across a cache cluster. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → Cluster Name | Channel cluster name. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → Address | Channel address. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → State Transfer | State transfer on the channel. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Channel → Message Dispatcher | Message dispatcher. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Protocol Order | Order of protocols in the stack. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Protocol Stack → Protocol Configuration | Per-protocol configuration. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport → Port | Transport port. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport → Bind Address | Transport bind address. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Transport → Buffer Size | Transport buffer size. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Discovery Protocol → Initial Hosts | Initial hosts for discovery. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Failure Detection → Timeout | Failure-detection timeout. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Failure Detection → Max Attempts | Maximum failure-detection attempts. |
| `Production Technical System` → WildFly → Subsystems → JGroups → MERGE3 → Merge Interval | Merge interval. |
| `Production Technical System` → WildFly → Subsystems → JGroups → FD_SOCK → Client Bind Address | FD_SOCK client bind address. |
| `Production Technical System` → WildFly → Subsystems → JGroups → Reliable Group Communication | Exchanging messages over channels with delivery guarantees. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Node → Name | Cluster node name. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Node → Address | Cluster node address. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → Coordinator | Cluster coordinator. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → View | Cluster view. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Cluster Membership → Node List | List of cluster members. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Distributed Session Management → Session Cache | Distributed session cache. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Distributed Session Management → Session Ownership | Session ownership. |
| `Production Technical System` → WildFly → Subsystems → Clustering → Session State Replication | Replicating session state across cluster nodes. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Management → Session Access | Session access. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Affinity → Node Selection | Node-selection algorithm. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Replication → Replication Mode | Replication mode. |
| `Production Technical System` → WildFly → Subsystems → Distributable Web → Session Replication → Replication Granularity | Replication granularity. |
| `Production Technical System` → WildFly → Subsystems → Distributable EJB → State Replication | EJB state replication. |
| `Production Technical System` → WildFly → Subsystems → Distributable EJB → Failover | EJB failover. |
| `Production Technical System` → WildFly → Subsystems → Distributable EJB → Load Balancing | EJB load balancing. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Service → Service Name | Singleton service name. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Service → Provider | Singleton provider. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Policy → Policy Name | Singleton policy name. |
| `Production Technical System` → WildFly → Subsystems → Singleton → Singleton Election | Electing the active singleton service among members. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Transaction ID | Transaction identifier. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Transaction Status | Transaction status. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction Manager → Transaction Timeout | Transaction timeout. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction → Resource Enlistment | Resource enlistment. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction → Synchronization | Transaction synchronization. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Transaction → Branch | Transaction branch. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → XA Resource | XA resource. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → XA Branch | XA branch. |
| `Production Technical System` → WildFly → Subsystems → Transactions → XA Coordination → XID | XA transaction identifier. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Manager → Scan Interval | Recovery scan interval. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Manager → Recovery Module | Recovery module. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Scan → In-Doubt Transaction | In-doubt transaction. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Recovery → Recovery Scan → Heuristic Outcome | Heuristic outcome. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Transaction Log → Log File | Transaction log file. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Transaction Log → Log Entry | Transaction log entry. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Write → Append | Append to log. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Write → Sync | Sync log write. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Read → Scan | Scan log file. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Object Store → Log Read → Replay | Replay log entry. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout → Transaction Timeout → Timeout Value | Timeout value. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout → Reaper → Reaper Thread | Reaper thread. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Timeout → Reaper → Reaper Interval | Reaper interval. |
| `Production Technical System` → WildFly → Subsystems → Transactions → JTS → ORB Integration → ORB | ORB instance. |
| `Production Technical System` → WildFly → Subsystems → Transactions → JTS → ORB Integration → POA | Portable Object Adapter. |
| `Production Technical System` → WildFly → Subsystems → Transactions → JTS → ORB Integration → IOR | Interoperable Object Reference. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Suspended Execution | Suspending and resuming transactional work across contexts. |
| `Production Technical System` → WildFly → Subsystems → Transactions → Two-Phase Commit | Coordinating resource commitment in prepare and commit phases. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Acceptors → In-VM Acceptor | In-VM acceptor. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Acceptors → Netty Acceptor | Netty acceptor. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Acceptors → HTTP Acceptor | HTTP acceptor. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Connectors → In-VM Connector | In-VM connector. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Connectors → Netty Connector | Netty connector. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Security Settings → Security Domain | Broker security domain. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Security Settings → Permission | Broker permission. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Persistence → Journal Type | Journal type. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Persistence → Journal Directory | Journal directory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Journal → Journal File | Journal file. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Journal → Journal Record | Journal record. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Broker Server → Journal → Journal Compaction | Journal compaction. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Address Name | Address name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Routing Type | Address routing type. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Bindings → Queue Binding | Queue binding. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address → Bindings → Topic Binding | Topic binding. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Queue Name | Queue name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Durable | Durable flag. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Max Consumers | Maximum consumers. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Consumers → Consumer | Queue consumer. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Queue → Messages → Message | Queued message. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Topic Name | Topic name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Durable Subscription | Durable subscription. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Non-Durable Subscription | Non-durable subscription. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Topic → Messages → Message | Topic message. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Factory Name | Connection-factory name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Connectors | Connectors used by the factory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Discovery Group | Discovery group. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → HA | High-availability flag. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Client ID | Client ID. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connection Factory → Reconnect Attempts | Reconnect attempts. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connector → Socket Binding | Connector socket binding. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Connector → Protocol | Connector protocol. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Remote Connector → Remote Socket Binding | Remote-connector socket binding. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Remote Connector → Remote Protocol | Remote-connector protocol. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Acceptor → Acceptor Name | Acceptor name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Acceptor → Socket Binding | Acceptor socket binding. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Acceptor → Protocol | Acceptor protocol. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory → Pool Name | Pool name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory → Max Pool Size | Maximum pool size. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory → Min Pool Size | Minimum pool size. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Pooled Connection Factory → Idle Timeout | Pool idle timeout. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Source → Source Connection Factory | Source connection factory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Source → Source Destination | Source destination. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Target → Target Connection Factory | Target connection factory. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Target → Target Destination | Target destination. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Quality Of Service → QoS Mode | QoS mode. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → JMS Bridge → Quality Of Service → Failure Retry Interval | Failure-retry interval. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting → Authentication → User | Messaging user. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting → Authentication → Role | Messaging role. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Security Setting → Authorization → Permission | Messaging permission. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Address Match | Address match pattern. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Dead Letter Address → DLQ | Dead-letter queue. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Expiry Address → Expiry Queue | Expiry queue. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Max Size Bytes → Bytes | Maximum size in bytes. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Page Size Bytes | Page size in bytes. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Page Cache Max Size | Page-cache max size. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Address Setting → Message Counter History | Message-counter history. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Divert Name | Divert name. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Routing Type | Divert routing type. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Forwarding Address | Forwarding address. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Filter | Divert filter. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Divert → Transformer | Divert transformer. |
| `Production Technical System` → WildFly → Subsystems → Messaging-ActiveMQ → Message-Driven Delivery | Delivering messages asynchronously to consumers. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Archive | Resource-adapter archive. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Deployment Descriptor | Resource-adapter deployment descriptor. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Connection Factory → Managed Connection Factory | Managed connection factory. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Connection Factory → Connection Factory Interface | Connection factory interface. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Admin Object → Admin Object Interface | Admin-object interface. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Resource Adapter → Admin Object → Admin Object Properties | Admin-object properties. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Managed Connection Factory → Connection Factory Impl | Connection-factory implementation. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Managed Connection Factory → Connection Impl | Connection implementation. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Connection Factory Interface → Interface Class | Interface class. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Definition → Connection Interface → Interface Class | Connection interface class. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Admin Object → Admin Object Interface → Interface Class | Admin-object interface class. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Admin Object → Admin Object Properties → Property | Admin-object property. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Activation → Activation Spec → Message Listener Type | Message-listener type. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Activation → Message Listener → OnMessage | Message-listener callback. |
| `Production Technical System` → WildFly → Subsystems → Resource Adapters → Connection Establishment | Establishing managed connections from definitions. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Authentication → Login Module | Legacy login module. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Authentication → JAAS Configuration | JAAS configuration. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Authorization → Role Mapping | Role mapping. |
| `Production Technical System` → WildFly → Subsystems → Security → Legacy Security Domain → Mapping → Principal Mapping | Principal mapping. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Default Realm → Realm Name | Default realm name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Role Decoder → Decoder Name | Role-decoder name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Domain → Permission Mapper → Mapper Name | Permission-mapper name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm → Name | Realm name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm → Identity Acquisition → Identity | Identity acquisition. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Security Realm → Credential Acquisition → Credential | Credential acquisition. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Identity Realm → Identity Store → Identity Entry | Identity entry. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Identity Realm → Identity Store → Attribute | Identity attribute. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Filesystem Realm → Filesystem Store → File | Identity file. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Filesystem Realm → Filesystem Store → Directory | Identity directory. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Filesystem Realm → Filesystem Store → Level | Filesystem level. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JDBC Realm → SQL Query → Principal Query | Principal query. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JDBC Realm → SQL Query → Role Query | Role query. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JDBC Realm → SQL Query → Attribute Query | Attribute query. |
| `Production Technical System` → WildFly → Subsystems → Elytron → LDAP Realm → LDAP Search → Search Base | LDAP search base. |
| `Production Technical System` → WildFly → Subsystems → Elytron → LDAP Realm → LDAP Search → Filter | LDAP search filter. |
| `Production Technical System` → WildFly → Subsystems → Elytron → JAAS Realm → Login Context → Login Module | JAAS login module. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Aggregate Realm → Realm Composition → Realm Order | Realm order. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Caching Realm → Cache → Cache Size | Cache size. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Caching Realm → Cache → Cache Timeout | Cache timeout. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Key Entry → Alias | Key alias. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Key Entry → Key Algorithm | Key algorithm. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Key Entry → Key Size | Key size. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Certificate Entry → Alias | Certificate alias. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Key Store → Certificate Entry → Certificate | Certificate. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Trust Store → Trusted Certificate → Alias | Trusted-certificate alias. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Trust Store → Trusted Certificate → Certificate | Trusted certificate. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Credential Store → Credential Entry → Alias | Credential alias. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Credential Store → Credential Entry → Secret | Credential secret. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Authentication Factory → Mechanism Selection → Mechanism Name | Authentication-mechanism name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → HTTP Authentication Factory → HTTP Mechanism → Mechanism Name | HTTP authentication-mechanism name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → SASL Authentication Factory → SASL Mechanism → Mechanism Name | SASL mechanism name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Permission Mapper → Permission Assignment → Permission | Assigned permission. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Role Mapper → Role Transformation → Role | Transformed role. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Principal Transformer → Principal Transformation → Principal | Transformed principal. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Evidence Decoder → Evidence Decoding → Evidence Type | Evidence type. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Realm Mapper → Realm Mapping → Realm Name | Realm name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Protocol Selection → Protocol | TLS protocol. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Cipher Suite Selection → Cipher Suite | Cipher suite. |
| `Production Technical System` → WildFly → Subsystems → Elytron → TLS Configuration → Certificate Revocation → Revocation Check | Revocation check. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Cipher Suite → Cipher Name → Name | Cipher-suite name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Protocol → Protocol Name → Name | Protocol name. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Validation → Signature | Token signature. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Validation → Expiry | Token expiry. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Validation → Issuer | Token issuer. |
| `Production Technical System` → WildFly → Subsystems → Elytron → OIDC Client → Token Refresh → Refresh Token | Refresh token. |
| `Production Technical System` → WildFly → Subsystems → Elytron → Authentication Composition | Assembling authentication from factories, mappers, and realms. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Service Endpoint Interface | Service endpoint interface. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Implementation Class | Endpoint implementation class. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Binding | SOAP binding. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Handler Chain | SOAP handler chain of the endpoint. |
| `Production Technical System` → WildFly → Subsystems → Web Services → JAX-WS Endpoint → Handler Chain → Handler | SOAP handler. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Service Definition → Port | WSDL port. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Binding Definition → Operation | WSDL binding operation. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Port Type Definition → Operation | WSDL port-type operation. |
| `Production Technical System` → WildFly → Subsystems → Web Services → WSDL → Message Definition → Part | WSDL message part. |
| `Production Technical System` → WildFly → Subsystems → Web Services → Handler Chain → Handler Invocation → Inbound | Inbound handler invocation. |
| `Production Technical System` → WildFly → Subsystems → Web Services → Handler Chain → Handler Invocation → Outbound | Outbound handler invocation. |
| `Production Technical System` → WildFly → Subsystems → Web Services → Endpoint Publication | Publishing SOAP endpoints from deployments. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Instance → Instance ID | Job-instance ID. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Execution → Execution ID | Job-execution ID. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Execution → Batch Status | Batch status. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job → Job Execution → Exit Status | Exit status. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Step Execution → Step Name | Step name. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Chunk Processing → Reader | Chunk reader. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Chunk Processing → Processor | Chunk processor. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Chunk Processing → Writer | Chunk writer. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Chunk Processing → Checkpoint | Chunk checkpoint. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Step → Batchlet Processing → Batchlet | Batchlet. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Repository → Job State → Job Instance | Job instance. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Repository → Step State → Step Execution | Step execution. |
| `Production Technical System` → WildFly → Subsystems → Batch JBeret → Job Execution | Executing batch jobs through ordered steps. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Session Properties → Host | Mail host. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Session Properties → Port | Mail port. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Session Properties → Protocol | Mail protocol. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Session Properties → Debug | Debug flag. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Credentials → User | Mail user. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Session → Credentials → Password | Mail password. |
| `Production Technical System` → WildFly → Subsystems → Mail → Mail Dispatch | Dispatching messages through mail sessions. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Attribute → Name | MBean attribute name. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Attribute → Type | MBean attribute type. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Operation → Name | MBean operation name. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Operation → Signature | MBean operation signature. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean → Notification → Type | Notification type. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Server → Registration → Object Name | MBean object name. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Server → Query → Query Expression | JMX query expression. |
| `Production Technical System` → WildFly → Subsystems → JMX → JMX Connector → Remote Access → RMI | RMI-based JMX access. |
| `Production Technical System` → WildFly → Subsystems → JMX → MBean Registration | Registering managed objects with the MBean server. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Level → Level Value | Log-level value. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Handlers → Handler Reference | Handler reference. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Category → Use Parent Handlers → Flag | Use-parent-handlers flag. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Level → Level Value | Handler-level value. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Formatter → Pattern | Formatter pattern. |
| `Production Technical System` → WildFly → Subsystems → Logging → Handler → Filter → Expression | Filter expression. |
| `Production Technical System` → WildFly → Subsystems → Logging → File Handler → File Path → Path | Log-file path. |
| `Production Technical System` → WildFly → Subsystems → Logging → File Handler → Append → Flag | Append flag. |
| `Production Technical System` → WildFly → Subsystems → Logging → Console Handler → Target → Target | Console target. |
| `Production Technical System` → WildFly → Subsystems → Logging → Periodic Rotating File Handler → Suffix → Suffix Pattern | Rotation suffix. |
| `Production Technical System` → WildFly → Subsystems → Logging → Size Rotating File Handler → Max File Size → Size | Max file size. |
| `Production Technical System` → WildFly → Subsystems → Logging → Size Rotating File Handler → Max Backup Index → Index | Max backup index. |
| `Production Technical System` → WildFly → Subsystems → Logging → Async Handler → Queue Length → Length | Async queue length. |
| `Production Technical System` → WildFly → Subsystems → Logging → Async Handler → Overflow Action → Action | Overflow action. |
| `Production Technical System` → WildFly → Subsystems → Logging → Formatter → Pattern → Format | Format pattern. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Level → Severity → Severity | Severity threshold. |
| `Production Technical System` → WildFly → Subsystems → Logging → Log Routing And Formatting | Routing records to handlers and formatting output. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker → Task Queue → Queue | Worker task queue. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker → Thread Pool → Threads | Worker threads. |
| `Production Technical System` → WildFly → Subsystems → IO → Buffer Pool → Buffer Size → Size | Buffer size. |
| `Production Technical System` → WildFly → Subsystems → IO → Buffer Pool → Buffer Count → Count | Buffer count. |
| `Production Technical System` → WildFly → Subsystems → IO → Worker Dispatch | Dispatching I/O work to thread workers. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Connector → Transport → Transport Type | Transport type. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Connector → Security → SASL Policy | Connector SASL policy. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Endpoint → Listener → Listener Type | Listener type. |
| `Production Technical System` → WildFly → Subsystems → Remoting → HTTP Upgrade → Upgrade Handshake → Upgrade Header | HTTP upgrade header. |
| `Production Technical System` → WildFly → Subsystems → Remoting → SASL Policy → Mechanism Selection → Mechanism | SASL mechanism. |
| `Production Technical System` → WildFly → Subsystems → Remoting → Remote Invocation | Invoking components across process boundaries. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Discovery Provider → Static Provider → Address List | Static address list. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Discovery Provider → Aggregate Provider → Providers | Aggregated providers. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Static Discovery → Address List → Address | Static address. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Aggregate Discovery → Provider Composition → Provider | Aggregated provider. |
| `Production Technical System` → WildFly → Subsystems → Discovery → Service Discovery | Locating remote services through providers. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Proxy → Balancer → Balancer Type | Balancer type. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Proxy → Node Registration → Node | Registered node. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise → Multicast → Multicast Address | Multicast address. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise → Multicast → Multicast Port | Multicast port. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Advertise → Socket Advertisement → Socket Binding | Advertisement socket binding. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Balancer → Load Factor → Factor | Load factor. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Balancer → Sticky Session → Sticky | Sticky-session flag. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Node → Node Registration → Node | Registered node. |
| `Production Technical System` → WildFly → Subsystems → Mod_Cluster → Load Distribution | Distributing traffic across cluster nodes. |
| `Production Technical System` → WildFly → Subsystems → Health → Health Check → UP → Status | UP status. |
| `Production Technical System` → WildFly → Subsystems → Health → Health Check → DOWN → Status | DOWN status. |
| `Production Technical System` → WildFly → Subsystems → Health → Readiness Check → READY → Status | READY status. |
| `Production Technical System` → WildFly → Subsystems → Health → Readiness Check → NOT_READY → Status | NOT_READY status. |
| `Production Technical System` → WildFly → Subsystems → Health → Liveness Check → ALIVE → Status | ALIVE status. |
| `Production Technical System` → WildFly → Subsystems → Health → Liveness Check → DEAD → Status | DEAD status. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Metric → Value → Value | Metric value. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Metric → Unit → Unit | Metric unit. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Gauge → Reading → Reading | Gauge reading. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Counter → Increment → Delta | Counter increment. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Counter → Decrement → Delta | Counter decrement. |
| `Production Technical System` → WildFly → Subsystems → Metrics → Histogram → Buckets → Bucket | Histogram bucket. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Config → Property Source → Source Name | Property-source name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Config → Property Value → Value | Property value. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Health → Health Check → Check Name | Health-check name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Retry → Max Retries | Maximum retries. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Retry → Delay | Retry delay. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Timeout → Timeout Value | Timeout value. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Circuit Breaker → Failure Threshold | Failure threshold. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Circuit Breaker → Delay | Circuit-breaker delay. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Bulkhead → Max Concurrent | Maximum concurrent calls. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Bulkhead → Queue Size | Bulkhead queue size. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Fault Tolerance → Fallback → Fallback Method | Fallback method. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Reactive Messaging → Channel → Channel Name | Channel name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Reactive Messaging → Connector → Connector Name | Connector name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → Metrics → Metric → Metric Name | Metric name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI → Document → Info | OpenAPI info section. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI → Document → Paths | OpenAPI paths section. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → OpenAPI → Operation → Operation ID | OpenAPI operation ID. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Token → Header | JWT header. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Token → Payload | JWT payload. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Claim → Claim Name | JWT claim name. |
| `Production Technical System` → WildFly → Subsystems → MicroProfile → JWT → Claim → Claim Value | JWT claim value. |
| `Production Technical System` → WildFly → Subsystems → SAR → SAR Deployment → Deployment → Archive | SAR archive. |
| `Production Technical System` → WildFly → Subsystems → SAR → SAR Deployment → Undeployment → Archive | SAR archive. |
| `Production Technical System` → WildFly → Subsystems → SAR → MBean → Registration → Object Name | SAR MBean object name. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Restore View | JSF restore-view phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Apply Request Values | JSF apply-request-values phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Process Validations | JSF process-validations phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Update Model Values | JSF update-model-values phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Invoke Application | JSF invoke-application phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Lifecycle → Render Response | JSF render-response phase. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Component Tree → UIViewRoot | JSF UIViewRoot. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Component Tree → UIComponent | JSF UIComponent. |
| `Production Technical System` → WildFly → Subsystems → JSF → Mojarra → Renderer → RenderKit | JSF RenderKit. |
| `Production Technical System` → WildFly → Subsystems → JSF → `faces-config.xml` → Navigation Rules → Rule | JSF navigation rule. |
| `Production Technical System` → WildFly → Subsystems → JSF → `faces-config.xml` → Managed Beans → Bean | JSF managed bean. |
| `Production Technical System` → WildFly → Subsystems → JSF → View Rendering | Rendering component trees into responses. |
| `Production Technical System` → WildFly → Subsystems → POJO → POJO Deployment → Deployment → Archive | POJO archive. |
| `Production Technical System` → WildFly → Subsystems → POJO → POJO Deployment → Undeployment → Archive | POJO archive. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Validator → Validation → Constraint Validation | Constraint validation. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint → Definition → Annotation | Constraint annotation. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint → Violation → Message | Violation message. |
| `Production Technical System` → WildFly → Subsystems → Bean Validation → Constraint Validation | Validating beans against constraints. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Scan → Directory Scan | Directory scan. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Deploy → Marker Handling | Marker handling. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Undeploy → Marker Handling | Marker handling. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Scan Interval → Interval | Scan interval. |
| `Production Technical System` → WildFly → Subsystems → Deployment Scanner → Deployment Marker → Type | Marker type. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Archive → File | Deployment archive file. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Descriptor → File | Deployment descriptor file. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit → Structure → Directory | Deployment directory. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF → `web.xml` | Servlet deployment descriptor. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF → `jboss-web.xml` | WildFly web descriptor. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF → `beans.xml` | CDI descriptor. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF → Classes | Compiled classes. |
| `Production Technical System` → WildFly → Deployment → WAR → WEB-INF → Libraries | Bundled libraries. |
| `Production Technical System` → WildFly → Deployment → WAR → META-INF → `MANIFEST.MF` | Manifest file. |
| `Production Technical System` → WildFly → Deployment → WAR → META-INF → Services | Service loader files. |
| `Production Technical System` → WildFly → Deployment → WAR → Static Content → HTML | Static HTML content. |
| `Production Technical System` → WildFly → Deployment → WAR → Static Content → CSS | Static CSS content. |
| `Production Technical System` → WildFly → Deployment → WAR → Static Content → JavaScript | Static JavaScript content. |
| `Production Technical System` → WildFly → Deployment → WAR → Static Content → Images | Static images. |
| `Production Technical System` → WildFly → Deployment → JAR → META-INF → `MANIFEST.MF` | Manifest file. |
| `Production Technical System` → WildFly → Deployment → JAR → META-INF → `persistence.xml` | Persistence descriptor. |
| `Production Technical System` → WildFly → Deployment → JAR → META-INF → `beans.xml` | CDI descriptor. |
| `Production Technical System` → WildFly → Deployment → JAR → Classes → Package | Java package. |
| `Production Technical System` → WildFly → Deployment → JAR → Classes → Class | Java class. |
| `Production Technical System` → WildFly → Deployment → JAR → Resources → Properties File | Properties file. |
| `Production Technical System` → WildFly → Deployment → JAR → Resources → XML File | XML resource. |
| `Production Technical System` → WildFly → Deployment → EAR → Modules → EJB Module | EJB module. |
| `Production Technical System` → WildFly → Deployment → EAR → Modules → Web Module | Web module. |
| `Production Technical System` → WildFly → Deployment → EAR → Modules → Connector Module | Connector module. |
| `Production Technical System` → WildFly → Deployment → EAR → Modules → Client Module | Client module. |
| `Production Technical System` → WildFly → Deployment → EAR → Libraries → Library JAR | Library JAR. |
| `Production Technical System` → WildFly → Deployment → EAR → META-INF → `application.xml` | Application descriptor. |
| `Production Technical System` → WildFly → Deployment → EAR → META-INF → `jboss-app.xml` | JBoss application descriptor. |
| `Production Technical System` → WildFly → Deployment → RAR → META-INF → `ra.xml` | Resource-adapter descriptor. |
| `Production Technical System` → WildFly → Deployment → RAR → META-INF → `ironjacamar.xml` | IronJacamar descriptor. |
| `Production Technical System` → WildFly → Deployment → RAR → Native Libraries → Library | Native library. |
| `Production Technical System` → WildFly → Deployment → SAR → META-INF → `jboss-service.xml` | Service descriptor. |
| `Production Technical System` → WildFly → Deployment → SAR → Service Classes → Service | Service class. |
| `Production Technical System` → WildFly → Deployment → Deployment Descriptor → Element → Element Name | Descriptor element name. |
| `Production Technical System` → WildFly → Deployment → Deployment Descriptor → Schema Reference → Namespace | Descriptor namespace. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Servlet Declaration → Servlet Name | Servlet name. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Servlet Declaration → Servlet Class | Servlet class. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Servlet Declaration → Init Parameter | Servlet init parameter. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Servlet Declaration → Load On Startup | Load-on-startup. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Filter Declaration → Filter Name | Filter name. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Filter Declaration → Filter Class | Filter class. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Listener Declaration → Listener Class | Listener class. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Welcome File → File | Welcome file. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Security Constraint → Role | Security role. |
| `Production Technical System` → WildFly → Deployment → `web.xml` → Security Constraint → URL Pattern | Security URL pattern. |
| `Production Technical System` → WildFly → Deployment → `jboss-web.xml` → Context Root → Root | Context root. |
| `Production Technical System` → WildFly → Deployment → `jboss-web.xml` → Virtual Host → Host | Virtual host. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Session Bean → Bean Name | Session-bean name. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Session Bean → Bean Class | Session-bean class. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Session Bean → Session Type | Session-bean type. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Message-Driven Bean → Bean Name | MDB name. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Message-Driven Bean → Destination | MDB destination. |
| `Production Technical System` → WildFly → Deployment → `ejb-jar.xml` → Assembly Descriptor → Security Role | EJB security role. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Persistence Unit → Unit Name | Persistence-unit name. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Persistence Unit → Transaction Type | Persistence transaction type. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Class List → Class | Persistence class. |
| `Production Technical System` → WildFly → Deployment → `persistence.xml` → Properties → Property | Persistence property. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Discovery Mode → Mode | Bean-discovery mode. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Interceptors → Interceptor | Interceptor class. |
| `Production Technical System` → WildFly → Deployment → `beans.xml` → Decorators → Decorator | Decorator class. |
| `Production Technical System` → WildFly → Deployment → `application.xml` → Module → Module URI | Module URI. |
| `Production Technical System` → WildFly → Deployment → `application.xml` → Security Role → Role | Application security role. |
| `Production Technical System` → WildFly → Deployment → `jboss-app.xml` → Class Loading → Policy | Class-loading policy. |
| `Production Technical System` → WildFly → Deployment → `ra.xml` → Resource Adapter → Adapter Class | Resource-adapter class. |
| `Production Technical System` → WildFly → Deployment → `ra.xml` → Connection Definition → Managed Connection Factory | Managed connection factory. |
| `Production Technical System` → WildFly → Deployment → `ironjacamar.xml` → Connection Pool → Pool Configuration | Connection-pool configuration. |
| `Production Technical System` → WildFly → Deployment → `application-client.xml` → Client Descriptor → Client Name | Client name. |
| `Production Technical System` → WildFly → Deployment → `jboss-client.xml` → Client Descriptor → Client Name | JBoss client name. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Dependencies → Module | Deployment module dependency. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Exclusions → Exclusion | Deployment exclusion. |
| `Production Technical System` → WildFly → Deployment → `jboss-deployment-structure.xml` → Local Resources → Resource | Local resource. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Class Annotation → Annotation | Class-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Method Annotation → Annotation | Method-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Annotation → Field Annotation → Annotation | Field-level annotation. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Parse → Descriptor Parser | Descriptor parser. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Parse → Annotation Scanner | Annotation scanner. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Register → Component Registry | Component registry. |
| `Production Technical System` → WildFly → Deployment → Deployment Processor → Deploy → Service Installation | Service installation. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → STRUCTURE → Structure Build | Structure build. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → PARSE → Parse | Parse phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → REGISTER → Register | Register phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → DEPENDENCIES → Dependency Resolution | Dependency resolution. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → CONFIGURE_MODULE → Module Configuration | Module configuration. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → POST_MODULE → Post-Module Processing | Post-module processing. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → INSTALL → Install | Install phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Phase → CLEANUP → Cleanup | Cleanup phase. |
| `Production Technical System` → WildFly → Deployment → Deployment Unit Processor → Transform → Transform Step | Transform step. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Registration → Service Name | Deployment-service name. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Start → Service Start | Service start. |
| `Production Technical System` → WildFly → Deployment → Deployment Service → Stop → Service Stop | Service stop. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Deploy → Transition | Deploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Undeploy → Transition | Undeploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Redeploy → Transition | Redeploy transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Replace → Transition | Replace transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Lifecycle → Explode → Transition | Explode transition. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Scan → Directory Scan | Directory scan. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Deploy → Marker Handling | Marker handling. |
| `Production Technical System` → WildFly → Deployment → Deployment Scanner → Undeploy → Marker Handling | Marker handling. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.dodeploy` → Marker | `.dodeploy` marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.undeploy` → Marker | `.undeploy` marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.deployed` → Marker | `.deployed` marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.failed` → Marker | `.failed` marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.isdeploying` → Marker | `.isdeploying` marker. |
| `Production Technical System` → WildFly → Deployment → Deployment Marker → `.skipdeploy` → Marker | `.skipdeploy` marker. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Classes → Class | Application class. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Resources → Resource | Application resource. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Libraries → Library | Application library. |
| `Production Technical System` → WildFly → Deployment → Application → Module → Class Loader → Loader | Application module class loader. |
| `Production Technical System` → WildFly → Deployment → Application → Component → Servlet Component → Servlet | Servlet component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → EJB Component → EJB | EJB component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → CDI Component → Bean | CDI bean component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → REST Component → Resource | REST resource component. |
| `Production Technical System` → WildFly → Deployment → Application → Component → WebSocket Component → Endpoint | WebSocket endpoint component. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Lifecycle → Init | Servlet init. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Lifecycle → Service | Servlet service. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Lifecycle → Destroy | Servlet destroy. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Request Handling → Request Dispatch | Servlet request dispatch. |
| `Production Technical System` → WildFly → Deployment → Application → Servlet → Session Handling → Session Access | Servlet session access. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Scope → Scope Annotation | CDI scope annotation. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Lifecycle → Creation | CDI bean creation. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Lifecycle → Destruction | CDI bean destruction. |
| `Production Technical System` → WildFly → Deployment → Application → CDI Bean → Injection → Injection Point | CDI injection point. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle → Creation | EJB creation. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle → Invocation | EJB invocation. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle → Passivation | EJB passivation. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle → Activation | EJB activation. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Lifecycle → Removal | EJB removal. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Business Interface → Interface | EJB business interface. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Transaction Attribute → Attribute | EJB transaction attribute. |
| `Production Technical System` → WildFly → Deployment → Application → EJB → Security Role → Role | EJB security role. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Resource Method → Method | REST resource method. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Path → Path | REST resource path. |
| `Production Technical System` → WildFly → Deployment → Application → REST Resource → Media Type → Media Type | REST media type. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Entity → Entity Class | JPA entity class. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Entity → Entity Mapping | JPA entity mapping. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Entity Manager Factory → Factory | Entity manager factory. |
| `Production Technical System` → WildFly → Deployment → Application → Persistence Unit → Data Source → DataSource | Data source. |
| `Production Technical System` → WildFly → Deployment → Application → JNDI Resource → Resource Reference → Reference Name | JNDI reference name. |
| `Production Technical System` → WildFly → Deployment → Application → JNDI Resource → Environment Entry → Entry Name | JNDI environment entry name. |
| `Production Technical System` → WildFly → Deployment → Application → Security Domain Association → Domain Reference → Domain | Security domain. |
| `Production Technical System` → WildFly → Deployment → Application → Datasource Dependency → Datasource Reference → Datasource | Datasource. |
| `Production Technical System` → WildFly → Deployment → Application → Messaging Dependency → Connection Factory Reference → Connection Factory | Connection factory. |
| `Production Technical System` → WildFly → Deployment → Application → Messaging Dependency → Destination Reference → Destination | Messaging destination. |
| `Production Technical System` → WildFly → Deployment → Application → Module Dependency → Module Reference → Module | WildFly module. |
| `Production Technical System` → WildFly → Deployment → Application → Module Dependency → Export → Package | Exported package. |
| `Production Technical System` → WildFly → Deployment → Archive Assembly | Technique for assembling deployment archives for WildFly deployment. |
| `Production Technical System` → WildFly → Services | Technical services delivered to deployed applications. |
| `Production Technical System` → WildFly → Services → Deployment Service | Controlled introduction and lifecycle of application deployments. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Capability | Possibility of deploying and running enterprise applications. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Interface | Boundary through which deployments are submitted: scanner, CLI, console. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Mechanism | Processor chain transforming deployment content into runtime services. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Activity | Sequence of submit, verify, and activate acts. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Task | Single deploy or undeploy unit of work. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Requirement | Deployments must reach active state within operational bounds. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Feedback | Deployment state, markers, and scanner notifications. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Evaluation | Determination of deployment success and health. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Maintenance | Redeploy, rollback, and content-repository upkeep. |
| `Production Technical System` → WildFly → Services → Deployment Service → Deployment Lifecycle | Deploy, operate, undeploy trajectory of a deployment. |
| `Production Technical System` → WildFly → Network → Public Interface → Inet Address → Address | Public inet address. |
| `Production Technical System` → WildFly → Network → Management Interface → Inet Address → Address | Management inet address. |
| `Production Technical System` → WildFly → Network → Unsecure Interface → Inet Address → Address | Unsecure inet address. |
| `Production Technical System` → WildFly → Network → HTTP Endpoint → Port → Port | HTTP port. |
| `Production Technical System` → WildFly → Network → HTTPS Endpoint → Port → Port | HTTPS port. |
| `Production Technical System` → WildFly → Network → HTTPS Endpoint → Certificate → Certificate | TLS certificate. |
| `Production Technical System` → WildFly → Network → AJP Endpoint → Port → Port | AJP port. |
| `Production Technical System` → WildFly → Network → Remoting Endpoint → Port → Port | Remoting port. |
| `Production Technical System` → WildFly → Network → Messaging Endpoint → Port → Port | Messaging port. |
| `Production Technical System` → WildFly → Network → JGroups Endpoint → Port → Port | JGroups port. |
| `Production Technical System` → WildFly → Network → TXN Recovery Endpoint → Port → Port | TXN recovery port. |
| `Production Technical System` → WildFly → Network → TXN Status Manager Endpoint → Port → Port | TXN status manager port. |
| `Production Technical System` → WildFly → Network → Management HTTP Endpoint → Port → Port | Management HTTP port. |
| `Production Technical System` → WildFly → Network → Management Native Endpoint → Port → Port | Management native port. |
| `Production Technical System` → WildFly → Network → Socket Binding → Name → Name | Socket-binding name. |
| `Production Technical System` → WildFly → Network → Socket Binding → Port → Port | Socket-binding port. |
| `Production Technical System` → WildFly → Network → Socket Binding → Interface → Interface | Socket-binding interface. |
| `Production Technical System` → WildFly → Network → Socket Binding Group → Default Interface → Interface | Default interface. |
| `Production Technical System` → WildFly → Network → Socket Binding Group → Port Offset → Offset | Port offset. |
| `Production Technical System` → WildFly → Network → Port Offset → Offset Value → Offset | Port offset value. |
| `Production Technical System` → WildFly → Network → Outbound Socket Binding → Remote Host → Host | Remote host. |
| `Production Technical System` → WildFly → Network → Outbound Socket Binding → Remote Port → Port | Remote port. |
| `Production Technical System` → WildFly → Network → Endpoint Binding | Constituting bound endpoints from configuration and interfaces. |
| `Production Technical System` → WildFly → Runtime Security → Authentication → Mechanism → Mechanism | Authentication mechanism. |
| `Production Technical System` → WildFly → Runtime Security → Authentication → Credential → Credential | Authentication credential. |
| `Production Technical System` → WildFly → Runtime Security → Authorization → Policy → Policy | Authorization policy. |
| `Production Technical System` → WildFly → Runtime Security → Authorization → Decision → Decision | Authorization decision. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Handshake → Handshake | TLS handshake. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Cipher Negotiation → Cipher | Negotiated cipher. |
| `Production Technical System` → WildFly → Runtime Security → TLS → Certificate Validation → Validation | Certificate validation. |
| `Production Technical System` → WildFly → Runtime Security → Credential Store → Entry → Entry | Credential entry. |
| `Production Technical System` → WildFly → Runtime Security → Credential Store → Alias → Alias | Credential alias. |
| `Production Technical System` → WildFly → Runtime Security → Identity → Name → Name | Identity name. |
| `Production Technical System` → WildFly → Runtime Security → Identity → Attributes → Attribute | Identity attribute. |
| `Production Technical System` → WildFly → Runtime Security → Principal → Name → Name | Principal name. |
| `Production Technical System` → WildFly → Runtime Security → Role → Name → Name | Role name. |
| `Production Technical System` → WildFly → Runtime Security → Permission → Name → Name | Permission name. |
| `Production Technical System` → WildFly → Runtime Security → Permission → Actions → Actions | Permission actions. |
| `Production Technical System` → WildFly → Runtime Security → Security Event → Type → Type | Security-event type. |
| `Production Technical System` → WildFly → Runtime Security → Security Event → Timestamp → Timestamp | Security-event timestamp. |
| `Production Technical System` → WildFly → Runtime Security → Audit Event → Category → Category | Audit-event category. |
| `Production Technical System` → WildFly → Runtime Security → Audit Event → Outcome → Outcome | Audit-event outcome. |
| `Production Technical System` → WildFly → Runtime Security → Security Domain → Name → Name | Security-domain name. |
| `Production Technical System` → WildFly → Runtime Security → Security Domain → Realm → Realm | Security-domain realm. |
| `Production Technical System` → WildFly → Runtime Security → Realm → Name → Name | Realm name. |
| `Production Technical System` → WildFly → Runtime Security → Realm → Identity Store → Store | Realm identity store. |
| `Production Technical System` → WildFly → Runtime Security → SSL Context → Protocol → Protocol | SSL context protocol. |
| `Production Technical System` → WildFly → Runtime Security → SSL Context → Cipher Suites → Cipher Suite | SSL context cipher suite. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Active Profile → Profile | Active profile. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Running Mode → Mode | Running mode. |
| `Production Technical System` → WildFly → Runtime Control → Configuration State → Server State → State | Server state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Started → State | Started state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Stopped → State | Stopped state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Reload Required → State | Reload-required state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime State → Restart Required → State | Restart-required state. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Name → Name | Runtime-metric name. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Value → Value | Runtime-metric value. |
| `Production Technical System` → WildFly → Runtime Control → Runtime Metric → Unit → Unit | Runtime-metric unit. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Level → Level | Log-event level. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Message → Message | Log-event message. |
| `Production Technical System` → WildFly → Runtime Control → Log Event → Timestamp → Timestamp | Log-event timestamp. |
| `Production Technical System` → WildFly → Runtime Control → Health Result → Status → Status | Health-result status. |
| `Production Technical System` → WildFly → Runtime Control → Health Result → Check → Check | Health-check name. |
| `Production Technical System` → WildFly → Runtime Control → Diagnostic Report → Section → Section | Diagnostic-report section. |
| `Production Technical System` → WildFly → Runtime Control → JDR → Collection → Collection | JDR collection. |
| `Production Technical System` → WildFly → Runtime Control → JDR → Report → Report | JDR report. |
| `Production Technical System` → WildFly → Runtime Control → Audit Log → Entry → Entry | Audit-log entry. |
| `Production Technical System` → WildFly → Runtime Control → Server Log → Entry → Entry | Server-log entry. |
| `Production Technical System` → WildFly → Runtime Control → GC Log → Entry → Entry | GC-log entry. |
| `Production Technical System` → WildFly → Runtime Control → Thread Dump → Thread → Thread | Dumped thread. |
| `Production Technical System` → WildFly → Runtime Control → Heap Dump → Heap Region → Region | Heap-dump region. |
| `Production Technical System` → WildFly → Lifecycle → Provision → Provisioning Plan → Plan | Provisioning plan. |
| `Production Technical System` → WildFly → Lifecycle → Provision → Provisioning Execution → Execution | Provisioning execution. |
| `Production Technical System` → WildFly → Lifecycle → Install → Distribution Extraction → Extraction | Distribution extraction. |
| `Production Technical System` → WildFly → Lifecycle → Install → File Placement → Placement | File placement. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Profile Selection → Selection | Profile selection. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Subsystem Configuration → Configuration | Subsystem configuration. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Interface Configuration → Configuration | Interface configuration. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Socket Binding Configuration → Configuration | Socket-binding configuration. |
| `Production Technical System` → WildFly → Lifecycle → Configure → Security Configuration → Configuration | Security configuration. |
| `Production Technical System` → WildFly → Lifecycle → Start → Service Container Start → Start | Service-container start. |
| `Production Technical System` → WildFly → Lifecycle → Start → Subsystem Start → Start | Subsystem start. |
| `Production Technical System` → WildFly → Lifecycle → Start → Deployment Start → Start | Deployment start. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Bootstrap → Bootstrap | Bootstrap. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Configuration Load → Load | Configuration load. |
| `Production Technical System` → WildFly → Lifecycle → Boot → Service Installation → Installation | Service installation. |
| `Production Technical System` → WildFly → Lifecycle → Deploy → Deployment Processing → Processing | Deployment processing. |
| `Production Technical System` → WildFly → Lifecycle → Deploy → Deployment Start → Start | Deployment start. |
| `Production Technical System` → WildFly → Lifecycle → Redeploy → Undeploy → Undeploy | Undeploy phase. |
| `Production Technical System` → WildFly → Lifecycle → Redeploy → Deploy → Deploy | Deploy phase. |
| `Production Technical System` → WildFly → Lifecycle → Reload → Stop → Stop | Reload stop. |
| `Production Technical System` → WildFly → Lifecycle → Reload → Start → Start | Reload start. |
| `Production Technical System` → WildFly → Lifecycle → Shutdown → Graceful Shutdown → Shutdown | Graceful shutdown. |
| `Production Technical System` → WildFly → Lifecycle → Shutdown → Forced Shutdown → Shutdown | Forced shutdown. |
| `Production Technical System` → WildFly → Lifecycle → Undeploy → Deployment Stop → Stop | Deployment stop. |
| `Production Technical System` → WildFly → Lifecycle → Undeploy → Content Removal → Removal | Content removal. |
| `Production Technical System` → WildFly → Lifecycle → Maintain → Corrective Maintenance → Maintenance | Corrective maintenance. |
| `Production Technical System` → WildFly → Lifecycle → Maintain → Preventive Maintenance → Maintenance | Preventive maintenance. |
| `Production Technical System` → WildFly → Lifecycle → Patch → Patch Application → Application | Patch application. |
| `Production Technical System` → WildFly → Lifecycle → Patch → Patch Verification → Verification | Patch verification. |
| `Production Technical System` → WildFly → Lifecycle → Upgrade → Version Change → Change | Version change. |
| `Production Technical System` → WildFly → Lifecycle → Upgrade → Configuration Migration → Migration | Configuration migration. |
| `Production Technical System` → WildFly → Lifecycle → Migrate → Configuration Transformation → Transformation | Configuration transformation. |
| `Production Technical System` → WildFly → Lifecycle → Migrate → Application Migration → Migration | Application migration. |
| `Production Technical System` → WildFly → Lifecycle → Retire → Decommissioning → Decommissioning | Decommissioning. |
| `Production Technical System` → WildFly → Lifecycle → Retire → Data Archival → Archival | Data archival. |
| `Production Technical System` → WildFly → Lifecycle → Rollback → Version Reversion → Reversion | Version reversion. |
| `Production Technical System` → WildFly → Lifecycle → Rollback → Configuration Reversion → Reversion | Configuration reversion. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Configuration Backup → Backup | Configuration backup. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Data Backup → Backup | Data backup. |
| `Production Technical System` → WildFly → Lifecycle → Backup → Deployment Backup → Backup | Deployment backup. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Configuration Restore → Restore | Configuration restore. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Data Restore → Restore | Data restore. |
| `Production Technical System` → WildFly → Lifecycle → Restore → Deployment Restore → Restore | Deployment restore. |
| `Production Technical System` → WildFly → External Resources → CPU → Core → Core | CPU core. |
| `Production Technical System` → WildFly → External Resources → CPU → Frequency → Frequency | CPU frequency. |
| `Production Technical System` → WildFly → External Resources → Memory → Heap → Heap | Runtime heap. |
| `Production Technical System` → WildFly → External Resources → Memory → Off-Heap → Off-Heap | Off-heap memory. |
| `Production Technical System` → WildFly → External Resources → Filesystem → Disk → Disk | Disk storage. |
| `Production Technical System` → WildFly → External Resources → Filesystem → Files → File | Accessed file. |
| `Production Technical System` → WildFly → External Resources → Network → Bandwidth → Bandwidth | Network bandwidth. |
| `Production Technical System` → WildFly → External Resources → Network → Latency → Latency | Network latency. |
| `Production Technical System` → WildFly → External Resources → Database → Connection → Connection | Database connection. |
| `Production Technical System` → WildFly → External Resources → Database → Storage → Storage | Database storage. |
| `Production Technical System` → WildFly → External Resources → Message Broker → Queue → Queue | Broker queue. |
| `Production Technical System` → WildFly → External Resources → Message Broker → Topic → Topic | Broker topic. |
| `Production Technical System` → WildFly → External Resources → Identity Provider → Realm → Realm | IdP realm. |
| `Production Technical System` → WildFly → External Resources → Identity Provider → Endpoint → Endpoint | IdP endpoint. |
| `Production Technical System` → WildFly → External Resources → Certificate Authority → Root Certificate → Root Certificate | Root certificate. |
| `Production Technical System` → WildFly → External Resources → Certificate Authority → CRL → CRL | Certificate revocation list. |
| `Production Technical System` → WildFly → External Resources → Load Balancer → Virtual IP → Virtual IP | Load-balancer virtual IP. |
| `Production Technical System` → WildFly → External Resources → Load Balancer → Pool → Pool | Backend pool. |
| `Production Technical System` → WildFly → External Resources → JDK → JRE → JRE | Java runtime environment. |
| `Production Technical System` → WildFly → External Resources → JDK → JDK Tools → Tool | JDK tool. |
| `Production Technical System` → WildFly → External Resources → Operating System → Kernel → Kernel | OS kernel. |
| `Production Technical System` → WildFly → External Resources → Operating System → Libraries → Library | OS library. |
| `Production Technical System` → WildFly → External Resources → Container Runtime → Image → Image | Container image. |
| `Production Technical System` → WildFly → External Resources → Container Runtime → Volume → Volume | Container volume. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Namespace → Namespace | Kubernetes namespace. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Service → Service | Kubernetes service. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → ConfigMap → ConfigMap | Kubernetes ConfigMap. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Secret → Secret | Kubernetes Secret. |
| `Production Technical System` → WildFly → External Resources → Kubernetes → Ingress → Ingress | Kubernetes Ingress. |
| `Production Technical System` → WildFly → Application Runtime Domain | Enterprise Java application-server runtime domain. |
| `Production Technical System` → WildFly → Application Runtime Domain → Undeployed Artifact Problem | Undeployed application artifacts require a managed, secure runtime to execute and integrate. |
| `Production Technical System` → WildFly → Application Runtime Domain → Managed Runtime Purpose | Provide a managed runtime for deploying, executing, integrating, securing, and managing enterprise applications. |
| `Production Technical System` → WildFly → Application Runtime Domain → JVM Compatibility | WildFly requires a compatible Java runtime version. |
| `Production Technical System` → WildFly → Application Runtime Domain → Resource Bounds | Execution is bounded by available CPU, memory, filesystem, and network capacity. |
| `Production Technical System` → WildFly → Application Runtime Domain → Specification Compliance | Subsystems must conform to Jakarta EE and related specifications. |
| `Production Technical System` → WildFly → Application Runtime Domain → Availability Objective | Sustained availability of deployed applications under expected load. |
| `Production Technical System` → WildFly → Application Runtime Domain → Deployment Responsiveness | Deployments must reach running state within operational time bounds. |
| `Production Technical System` → WildFly → Operators | Operators sustaining the WildFly instance. |
| `Production Technical System` → WildFly → Operators → Administrator | Human agent administering server configuration and lifecycle. |
| `Production Technical System` → WildFly → Operators → Application Deployer | Agent introducing application deployments into the runtime. |
| `Production Technical System` → WildFly → Operators → Provisioning Pipeline | Automated pipeline constructing and patching server installations. |
| `Production Technical System` → WildFly → Operators → Administration Effort | Purposive configuration, deployment, and maintenance effort. |
| `Production Technical System` → WildFly → Operators → Administration Expertise | Acquired capacity to reliably administer WildFly systems. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta EE → Profile → Profile | Jakarta EE profile. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Servlet → Version → Version | Jakarta Servlet version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta REST → Version → Version | Jakarta REST version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Enterprise Beans → Version → Version | Jakarta EJB version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Persistence → Version → Version | Jakarta Persistence version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Messaging → Version → Version | Jakarta Messaging version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta CDI → Version → Version | Jakarta CDI version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Transactions → Version → Version | Jakarta Transactions version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Bean Validation → Version → Version | Jakarta Bean Validation version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Batch → Version → Version | Jakarta Batch version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Concurrency → Version → Version | Jakarta Concurrency version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Connectors → Version → Version | Jakarta Connectors version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta Mail → Version → Version | Jakarta Mail version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta WebSocket → Version → Version | Jakarta WebSocket version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Binding → Version → Version | Jakarta JSON-B version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta JSON Processing → Version → Version | Jakarta JSON-P version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Binding → Version → Version | Jakarta XML Binding version. |
| `Production Technical System` → WildFly → Technical Standards → Jakarta XML Web Services → Version → Version | Jakarta XML WS version. |
| `Production Technical System` → WildFly → Technical Standards → JDBC → Version → Version | JDBC version. |
| `Production Technical System` → WildFly → Technical Standards → JNDI → Version → Version | JNDI version. |
| `Production Technical System` → WildFly → Technical Standards → JMX → Version → Version | JMX version. |
| `Production Technical System` → WildFly → Technical Standards → HTTP → Version → Version | HTTP version. |
| `Production Technical System` → WildFly → Technical Standards → HTTPS → Version → Version | HTTPS version. |
| `Production Technical System` → WildFly → Technical Standards → TLS → Version → Version | TLS version. |
| `Production Technical System` → WildFly → Technical Standards → AJP → Version → Version | AJP version. |
| `Production Technical System` → WildFly → Technical Standards → WebSocket → Version → Version | WebSocket version. |
| `Production Technical System` → WildFly → Technical Standards → OIDC → Version → Version | OIDC version. |
| `Production Technical System` → WildFly → Technical Standards → OAuth 2.0 → Version → Version | OAuth 2.0 version. |
| `Production Technical System` → WildFly → Technical Standards → SAML → Version → Version | SAML version. |
| `Production Technical System` → WildFly → Technical Standards → JWT → Version → Version | JWT version. |
| `Production Technical System` → WildFly → Technical Standards → MicroProfile → Version → Version | MicroProfile version. |
| `Production Technical System` → WildFly → Technical Standards → OpenAPI → Version → Version | OpenAPI version. |
| `Production Technical System` → WildFly → Technical Standards → OpenTelemetry → Version → Version | OpenTelemetry version. |
| `Production Technical System` → WildFly → Technical Practices → Provisioning → Plan Definition → Definition | Plan definition. |
| `Production Technical System` → WildFly → Technical Practices → Provisioning → Execution → Execution | Provisioning execution. |
| `Production Technical System` → WildFly → Technical Practices → Configuration Management → Change Control → Control | Change control. |
| `Production Technical System` → WildFly → Technical Practices → Configuration Management → Version Control → Control | Version control. |
| `Production Technical System` → WildFly → Technical Practices → Application Deployment → Release Process → Process | Release process. |
| `Production Technical System` → WildFly → Technical Practices → Application Deployment → Rollback Process → Process | Rollback process. |
| `Production Technical System` → WildFly → Technical Practices → Monitoring → Metric Collection → Collection | Metric collection. |
| `Production Technical System` → WildFly → Technical Practices → Monitoring → Alerting → Alerting | Alerting. |
| `Production Technical System` → WildFly → Technical Practices → Health Checking → Probe Scheduling → Scheduling | Probe scheduling. |
| `Production Technical System` → WildFly → Technical Practices → Health Checking → Result Handling → Handling | Result handling. |
| `Production Technical System` → WildFly → Technical Practices → Log Analysis → Collection → Collection | Log collection. |
| `Production Technical System` → WildFly → Technical Practices → Log Analysis → Interpretation → Interpretation | Log interpretation. |
| `Production Technical System` → WildFly → Technical Practices → Backup / Recovery → Backup Scheduling → Scheduling | Backup scheduling. |
| `Production Technical System` → WildFly → Technical Practices → Backup / Recovery → Restore Procedure → Procedure | Restore procedure. |
| `Production Technical System` → WildFly → Technical Practices → Patching → Patch Planning → Planning | Patch planning. |
| `Production Technical System` → WildFly → Technical Practices → Patching → Patch Application → Application | Patch application. |
| `Production Technical System` → WildFly → Technical Practices → Capacity Management → Sizing → Sizing | Capacity sizing. |
| `Production Technical System` → WildFly → Technical Practices → Capacity Management → Scaling → Scaling | Capacity scaling. |
| `Production Technical System` → WildFly → Technical Practices → Security Hardening → Exposure Reduction → Reduction | Exposure reduction. |
| `Production Technical System` → WildFly → Technical Practices → Security Hardening → Configuration Hardening → Hardening | Configuration hardening. |
| `Production Technical System` → WildFly → Technical Practices → Performance Tuning → JVM Tuning → Tuning | JVM tuning. |
| `Production Technical System` → WildFly → Technical Practices → Performance Tuning → Subsystem Tuning → Tuning | Subsystem tuning. |
| `Production Technical System` → WildFly → Technical Practices → Thread Management → Pool Sizing → Sizing | Thread-pool sizing. |
| `Production Technical System` → WildFly → Technical Practices → Thread Management → Queue Sizing → Sizing | Thread-queue sizing. |
| `Production Technical System` → WildFly → Technical Practices → Connection Pool Tuning → Pool Sizing → Sizing | Connection-pool sizing. |
| `Production Technical System` → WildFly → Technical Practices → Connection Pool Tuning → Timeout Tuning → Tuning | Timeout tuning. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → Heap Sizing → Sizing | Heap sizing. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → GC Selection → Selection | GC selection. |
| `Production Technical System` → WildFly → Technical Practices → JVM Tuning → System Property Tuning → Tuning | System-property tuning. |
| `Production Technical System` → WildFly → Design Rules | General rules governing construction and operation of this WildFly instance. |
| `Production Technical System` → WildFly → Design Rules → Least Privilege | Management and application access granted only as required. |
| `Production Technical System` → WildFly → Design Rules → Separation Of Concerns | Subsystems isolate distinct technical responsibilities. |
| `Production Technical System` → WildFly → Operating Strategies | Regimes for planning and allocating work on this WildFly instance. |
| `Production Technical System` → WildFly → Operating Strategies → Rolling Upgrade | Sequenced update of clustered servers preserving service availability. |
| `Production Technical System` → WildFly → Governing Bodies | Institutions governing this WildFly instance. |
| `Production Technical System` → WildFly → Governing Bodies → Jakarta EE Working Group | Body stewarding the enterprise specifications WildFly implements. |
| `Production Technical System` → WildFly → Governing Bodies → JBoss Community | Community sustaining WildFly knowledge, practice, and evolution. |
| `Production Technical System` → WildFly → Technical Dependencies → JVM → Java Version → Version | Required Java version. |
| `Production Technical System` → WildFly → Technical Dependencies → JVM → JVM Options → Option | Required JVM option. |
| `Production Technical System` → WildFly → Technical Dependencies → Operating System → OS Family → Family | Required OS family. |
| `Production Technical System` → WildFly → Technical Dependencies → Operating System → OS Libraries → Library | Required OS library. |
| `Production Technical System` → WildFly → Technical Dependencies → Filesystem → Paths → Path | Required filesystem path. |
| `Production Technical System` → WildFly → Technical Dependencies → Filesystem → Permissions → Permission | Required filesystem permission. |
| `Production Technical System` → WildFly → Technical Dependencies → Network Stack → Protocols → Protocol | Required network protocol. |
| `Production Technical System` → WildFly → Technical Dependencies → Network Stack → Ports → Port | Required network port. |
| `Production Technical System` → WildFly → Technical Dependencies → Database → JDBC Driver → Driver | Required JDBC driver. |
| `Production Technical System` → WildFly → Technical Dependencies → Database → Schema → Schema | Required database schema. |
| `Production Technical System` → WildFly → Technical Dependencies → External Services → Endpoint → Endpoint | Required external endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → External Services → Credentials → Credential | Required external credential. |
| `Production Technical System` → WildFly → Technical Dependencies → Message Broker → Broker Endpoint → Endpoint | Required broker endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → Message Broker → Destinations → Destination | Required destination. |
| `Production Technical System` → WildFly → Technical Dependencies → Identity Provider → IdP Endpoint → Endpoint | Required IdP endpoint. |
| `Production Technical System` → WildFly → Technical Dependencies → Identity Provider → Client Credentials → Credential | Required client credential. |
| `Production Technical System` → WildFly → Technical Dependencies → Certificate Authority → Root Certificate → Root Certificate | Required root certificate. |
| `Production Technical System` → WildFly → Technical Dependencies → Certificate Authority → Trust Chain → Chain | Required trust chain. |
| `Production Technical System` → WildFly → Technical Dependencies → Load Balancer → Frontend Address → Address | Required frontend address. |
| `Production Technical System` → WildFly → Technical Dependencies → Load Balancer → Backend Pool → Pool | Required backend pool. |
| `Production Technical System` → WildFly → Technical Dependencies → Container Runtime → Image → Image | Required container image. |
| `Production Technical System` → WildFly → Technical Dependencies → Container Runtime → Volume → Volume | Required container volume. |
| `Production Technical System` → WildFly → Technical Dependencies → Kubernetes API → API Server → Server | Required API server. |
| `Production Technical System` → WildFly → Technical Dependencies → Kubernetes API → Service Account → Account | Required service account. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Unit Test → Test Case | Unit test. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Integration Test → Test Case | Integration test. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Static Analysis → Analysis Report | Static analysis. |
| `Production Technical System` → WildFly → Technical Control → Verification Suite → Inspection → Inspection Record | Inspection. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → User Validation → Validation Outcome | User validation. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → Operational Trial → Trial Run | Operational trial. |
| `Production Technical System` → WildFly → Technical Control → Validation Suite → Acceptance Test → Test Case | Acceptance test. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Log Feedback → Log Record | Log feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Metric Feedback → Metric Reading | Metric feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Health Feedback → Health Report | Health feedback. |
| `Production Technical System` → WildFly → Technical Control → Feedback → Management State Feedback → State Snapshot | Management-state feedback. |
| `Production Technical System` → WildFly → Technical Control → Failure → Crash → Failure | Crash failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Hang → Failure | Hang failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Deadlock → Failure | Deadlock failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Memory Leak → Failure | Memory-leak failure. |
| `Production Technical System` → WildFly → Technical Control → Failure → Thread Leak → Failure | Thread-leak failure. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Exposed Voltage → Hazard | Exposed-voltage hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Thermal Runaway → Hazard | Thermal-runaway hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Race Condition → Hazard | Race-condition hazard. |
| `Production Technical System` → WildFly → Technical Control → Hazard → Resource Exhaustion → Hazard | Resource-exhaustion hazard. |
| `Production Technical System` → WildFly → Technical Control → Risk → Availability Risk → Risk | Availability risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Integrity Risk → Risk | Integrity risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Confidentiality Risk → Risk | Confidentiality risk. |
| `Production Technical System` → WildFly → Technical Control → Risk → Compliance Risk → Risk | Compliance risk. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Performance Vs Energy → Trade-Off | Performance-vs-energy trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Flexibility Vs Complexity → Trade-Off | Flexibility-vs-complexity trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Availability Vs Consistency → Trade-Off | Availability-vs-consistency trade-off. |
| `Production Technical System` → WildFly → Technical Control → Trade-Off → Security Vs Usability → Trade-Off | Security-vs-usability trade-off. |
| `Production Technical System` → WildFly → Technical Control → Performance → Response Time → Measurement | Response-time measurement. |
| `Production Technical System` → WildFly → Technical Control → Performance → Throughput → Measurement | Throughput measurement. |
| `Production Technical System` → WildFly → Technical Control → Performance → Resource Consumption → Measurement | Resource-consumption measurement. |
| `Production Technical System` → WildFly → Technical Control → Availability → Uptime → Measurement | Uptime measurement. |
| `Production Technical System` → WildFly → Technical Control → Availability → Downtime → Measurement | Downtime measurement. |
| `Production Technical System` → WildFly → Technical Control → Throughput → Requests Per Second → Metric | Requests-per-second metric. |
| `Production Technical System` → WildFly → Technical Control → Throughput → Bytes Per Second → Metric | Bytes-per-second metric. |
| `Production Technical System` → WildFly → Technical Control → Latency → P50 → Metric | Median latency. |
| `Production Technical System` → WildFly → Technical Control → Latency → P95 → Metric | 95th-percentile latency. |
| `Production Technical System` → WildFly → Technical Control → Latency → P99 → Metric | 99th-percentile latency. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → CPU Utilization → Metric | CPU-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Memory Utilization → Metric | Memory-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Disk Utilization → Metric | Disk-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Resource Utilization → Network Utilization → Metric | Network-utilization metric. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → HTTP 5xx Rate → Rate | HTTP 5xx error rate. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → Exception Rate → Rate | Exception rate. |
| `Production Technical System` → WildFly → Technical Control → Error Rate → Timeout Rate → Rate | Timeout rate. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Thread Pool Saturation → Saturation | Thread-pool saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Connection Pool Saturation → Saturation | Connection-pool saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Heap Saturation → Saturation | Heap saturation. |
| `Production Technical System` → WildFly → Technical Control → Saturation → Queue Saturation → Saturation | Queue saturation. |
| `Production Technical System` → WildFly → WildFly Ecosystem | Coherent body of server, tooling, configurations, and practices realizing managed Jakarta EE runtime capability. |

## How are the Java EE / Jakarta EE specifications implemented?

| Specification | Description | Implementation Detail |
| --- | --- | --- |
| Jakarta Servlet | Server-side web components: servlets, filters, listeners. | Undertow Servlet Container, Servlet, Filter (`org.wildfly.extension.undertow`) |
| Jakarta REST | REST endpoints with content negotiation. | RESTEasy, REST Endpoint, Jackson / JSON-B / JSON-P Providers (`org.wildfly.extension.jaxrs`) |
| Jakarta Enterprise Beans | Managed components with pooling, timers, remoting. | EJB3 Container, EJB Pool, Timer Service (`org.wildfly.extension.ejb3`) |
| Jakarta Persistence | Object-relational persistence units and entity management. | JPA, Hibernate ORM, Entity Manager, Second-Level Cache (`org.wildfly.extension.jpa`) |
| Jakarta Messaging | Queues, topics, pooled connection factories. | Messaging-ActiveMQ Broker Server, Queue, Topic, Pooled Connection Factory (`org.wildfly.extension.messaging-activemq`) |
| Jakarta CDI | Bean discovery, injection, interceptors, decorators. | CDI / Weld Bean Discovery, Dependency Injection, Interceptor, Decorator (`org.wildfly.extension.weld`) |
| Jakarta Dependency Injection | Injectable types and qualifiers. | CDI / Weld Dependency Injection, Producer Method |
| Jakarta Interceptors | Interception around business methods and lifecycle events. | CDI / Weld Interceptor; EJB3 interceptors |
| Jakarta Transactions | Distributed transaction coordination and recovery. | Transaction Manager, XA Coordination, Recovery (`org.wildfly.extension.transactions`) |
| Jakarta Bean Validation | Constraint declarations and validation runtime. | Validator, Constraint (`org.wildfly.extension.bean-validation`) |
| Jakarta Batch | Chunked batch jobs with steps and repositories. | Batch JBeret Job, Step, Job Repository (`org.wildfly.extension.batch.jberet`) |
| Jakarta Concurrency | Managed executors and context propagation. | Managed Executor Service, Context Service (EE subsystem) |
| Jakarta Connectors | Resource adapters with activation and connection definitions. | Resource Adapters, Activation, `ra.xml`, `ironjacamar.xml` |
| Jakarta Mail | Mail sessions for message dispatch. | Mail Session (`org.wildfly.extension.mail`) |
| Jakarta WebSocket | Full-duplex socket endpoints. | Undertow WebSocket, HTTP/HTTPS Listeners |
| Jakarta JSON Binding | JSON serialization binding. | RESTEasy JSON-B Provider |
| Jakarta JSON Processing | Streaming and object JSON processing. | RESTEasy JSON-P Provider |
| Jakarta XML Binding | XML binding for payloads. | RESTEasy JAXB Provider |
| Jakarta XML Web Services | SOAP endpoints with WSDL and handler chains. | JAX-WS Endpoint, WSDL, Handler Chain (`org.wildfly.extension.webservices`) |
| Jakarta Faces | Component-based server-side UI. | JSF, Mojarra, `faces-config.xml` (`org.wildfly.extension.jsf`) |
| Jakarta Server Pages | JSP page execution in the web container. | Undertow Servlet Container JSP support (no dedicated Jasper rows in this table yet) |
| Jakarta Expression Language | Unified expression evaluation in pages and CDI. | Provided via Faces/CDI integration (no dedicated rows) |
| Jakarta Security | Application security constraints and identity stores. | Elytron Security Domain, Security Realm (`org.wildfly.extension.elytron`) |
| Jakarta Authentication | HTTP/SASL authentication mechanisms. | Elytron HTTP/SASL Authentication Factory, OIDC Client |
| Jakarta Authorization | Role and permission decisions. | Elytron Role Mapper, Permission Mapper |
| Jakarta Annotations | Metadata-driven configuration. | Deployment Annotation processing (Class/Method/Field Annotation) |
| Jakarta Activation | Activation framework for data content. | No dedicated subsystem (provided transitively via Mail) |
| Jakarta Management | Standardized management model. | Not implemented as such (management via DMR model, HTTP/Native interfaces, JMX) |
| Jakarta Deployment | Standard deployment tooling API. | Not implemented as such (deployment via Deployment Scanner, CLI, console) |
| JDBC | Relational access through managed pools. | Datasource, XA Datasource, Connection Pool, JDBC Driver (`org.wildfly.extension.datasources-agroal`) |
| JNDI | Naming and directory lookup. | Naming, JNDI Namespace, JNDI Binding (`org.wildfly.extension.naming`) |
| JMX | Managed beans and remote management. | MBean, MBean Server (`org.wildfly.extension.jmx`) |
| HTTP/HTTPS | Web transport listeners. | Undertow HTTP/HTTPS Listeners, Socket Binding |
| TLS | Transport security for endpoints and remoting. | Elytron TLS Configuration, Cipher Suite; Runtime Security TLS |
| MicroProfile Config/Health/Metrics | Externalized config, probes, telemetry. | MicroProfile Config/Health/Metrics (`org.wildfly.extension.microprofile.*-smallrye`, `…metrics`) |
| MicroProfile Fault Tolerance | Retries, bulkheads, circuit breaking. | Fault Tolerance mechanisms (`org.wildfly.extension.microprofile.fault-tolerance-smallrye`) |
| MicroProfile JWT | Token-based authentication. | JWT authentication capability (MicroProfile) |
| MicroProfile OpenAPI | API description generation. | OpenAPI generation (`org.wildfly.extension.microprofile.openapi-smallrye`) |
| MicroProfile Reactive Messaging | Reactive message channels. | Reactive Messaging capability (`org.wildfly.extension.microprofile.reactive-messaging-smallrye`) |
| OpenTelemetry | Distributed tracing and metrics export. | OpenTelemetry/Micrometer extensions, Metrics subsystem |

## Configuration File(s)

```csharp
- ls bin/standalone.sh
- ls bin/standalone.conf
- ls standalone/configuration/standalone.xml
```

## Admin User

```bash
./bin/add-user.sh
./bin/add-user.sh -u admin -p NEW_PASSWORD
```

## QA

### How does WildFly handle the situation when the user provides WildFly module libraries?

### What is the structure (Architecture) of Wildfly?

### What is a provider `org.jboss.resteasy.plugins.providers.jackson.ResteasyJackson2Provider`?

### What is the role of the web.xml, jboss-deployment-structure.xml and jboss-web.xml?

### What is JSON-B?

### How can we detect library drift between the development libraries (usually not the API) and the libraries provided by the application container?

### How to create the pom - dependency tree of a Maven Project?

### What is an application container? What characteristics must it have in order to be considered one?

## References

- [WildFly](https://www.wildfly.org/)
- [WildFly Source Code](https://github.com/wildfly/wildfly/)
- [WildFly Core](https://github.com/wildfly/wildfly-core/tree/main)
- [JBoss Modules](https://github.com/jboss-modules/jboss-modules)
- [Distributed System Lab — Jakarta EE](https://github.com/dbremont/distributed-system-lab/tree/main/jakarta-ee)
