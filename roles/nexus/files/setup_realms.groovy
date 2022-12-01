import groovy.json.JsonSlurper
import org.sonatype.nexus.security.realm.RealmManager

parsed_args = new JsonSlurper().parseText(args)

realmManager = container.lookup(RealmManager.class.getName())

// enable/disable the Docker Bearer Token Realm
realmManager.enableRealm("DockerToken", parsed_args.docker_bearer_token_realm)
