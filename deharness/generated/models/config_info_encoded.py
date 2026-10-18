from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.config_info_encoded_share import ConfigInfoEncodedShare
from ..models.config_info_encoded_update import ConfigInfoEncodedUpdate
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded_agents import ConfigInfoEncodedAgents
  from ..models.config_info_encoded_commands import ConfigInfoEncodedCommands
  from ..models.config_info_encoded_compaction import ConfigInfoEncodedCompaction
  from ..models.config_info_encoded_enterprise import ConfigInfoEncodedEnterprise
  from ..models.config_info_encoded_experimental import ConfigInfoEncodedExperimental
  from ..models.config_info_encoded_formatter_type_1 import ConfigInfoEncodedFormatterType1
  from ..models.config_info_encoded_lsp_type_1 import ConfigInfoEncodedLspType1
  from ..models.config_info_encoded_mcp import ConfigInfoEncodedMcp
  from ..models.config_info_encoded_media import ConfigInfoEncodedMedia
  from ..models.config_info_encoded_model_type_1 import ConfigInfoEncodedModelType1
  from ..models.config_info_encoded_policies_item import ConfigInfoEncodedPoliciesItem
  from ..models.config_info_encoded_providers import ConfigInfoEncodedProviders
  from ..models.config_info_encoded_references import ConfigInfoEncodedReferences
  from ..models.config_info_encoded_tool_output import ConfigInfoEncodedToolOutput
  from ..models.config_info_encoded_watcher import ConfigInfoEncodedWatcher
  from ..models.config_plugin_entry_encoded import ConfigPluginEntryEncoded
  from ..models.config_warming_encoded import ConfigWarmingEncoded
  from ..models.config_web_search_info_encoded import ConfigWebSearchInfoEncoded
  from ..models.config_worktree import ConfigWorktree
  from ..models.permission_rule import PermissionRule





T = TypeVar("T", bound="ConfigInfoEncoded")



@_attrs_define
class ConfigInfoEncoded:
    """ 
        Attributes:
            schema (str | Unset):
            agents (ConfigInfoEncodedAgents | Unset):
            commands (ConfigInfoEncodedCommands | Unset):
            compaction (ConfigInfoEncodedCompaction | Unset):
            default_agent (str | Unset):
            enterprise (ConfigInfoEncodedEnterprise | Unset):
            experimental (ConfigInfoEncodedExperimental | Unset):
            formatter (bool | ConfigInfoEncodedFormatterType1 | Unset):
            instructions (list[str] | Unset):
            lsp (bool | ConfigInfoEncodedLspType1 | Unset):
            mcp (ConfigInfoEncodedMcp | Unset):
            media (ConfigInfoEncodedMedia | Unset):
            model (ConfigInfoEncodedModelType1 | str | Unset):
            permissions (list[PermissionRule] | Unset):
            plugins (list[ConfigPluginEntryEncoded | str] | Unset):
            policies (list[ConfigInfoEncodedPoliciesItem] | Unset):
            providers (ConfigInfoEncodedProviders | Unset):
            references (ConfigInfoEncodedReferences | Unset):
            share (ConfigInfoEncodedShare | Unset):
            shell (str | Unset):
            skills (list[str] | Unset):
            snapshots (bool | Unset):
            tool_output (ConfigInfoEncodedToolOutput | Unset):
            update (ConfigInfoEncodedUpdate | Unset):
            username (str | Unset):
            warming (bool | ConfigWarmingEncoded | Unset):
            watcher (ConfigInfoEncodedWatcher | Unset):
            websearch (bool | ConfigWebSearchInfoEncoded | Unset):
            worktree (ConfigWorktree | Unset):
     """

    schema: str | Unset = UNSET
    agents: ConfigInfoEncodedAgents | Unset = UNSET
    commands: ConfigInfoEncodedCommands | Unset = UNSET
    compaction: ConfigInfoEncodedCompaction | Unset = UNSET
    default_agent: str | Unset = UNSET
    enterprise: ConfigInfoEncodedEnterprise | Unset = UNSET
    experimental: ConfigInfoEncodedExperimental | Unset = UNSET
    formatter: bool | ConfigInfoEncodedFormatterType1 | Unset = UNSET
    instructions: list[str] | Unset = UNSET
    lsp: bool | ConfigInfoEncodedLspType1 | Unset = UNSET
    mcp: ConfigInfoEncodedMcp | Unset = UNSET
    media: ConfigInfoEncodedMedia | Unset = UNSET
    model: ConfigInfoEncodedModelType1 | str | Unset = UNSET
    permissions: list[PermissionRule] | Unset = UNSET
    plugins: list[ConfigPluginEntryEncoded | str] | Unset = UNSET
    policies: list[ConfigInfoEncodedPoliciesItem] | Unset = UNSET
    providers: ConfigInfoEncodedProviders | Unset = UNSET
    references: ConfigInfoEncodedReferences | Unset = UNSET
    share: ConfigInfoEncodedShare | Unset = UNSET
    shell: str | Unset = UNSET
    skills: list[str] | Unset = UNSET
    snapshots: bool | Unset = UNSET
    tool_output: ConfigInfoEncodedToolOutput | Unset = UNSET
    update: ConfigInfoEncodedUpdate | Unset = UNSET
    username: str | Unset = UNSET
    warming: bool | ConfigWarmingEncoded | Unset = UNSET
    watcher: ConfigInfoEncodedWatcher | Unset = UNSET
    websearch: bool | ConfigWebSearchInfoEncoded | Unset = UNSET
    worktree: ConfigWorktree | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded_agents import ConfigInfoEncodedAgents # noqa: PLC0415
        from ..models.config_info_encoded_commands import ConfigInfoEncodedCommands # noqa: PLC0415
        from ..models.config_info_encoded_compaction import ConfigInfoEncodedCompaction # noqa: PLC0415
        from ..models.config_info_encoded_enterprise import ConfigInfoEncodedEnterprise # noqa: PLC0415
        from ..models.config_info_encoded_experimental import ConfigInfoEncodedExperimental # noqa: PLC0415
        from ..models.config_info_encoded_formatter_type_1 import ConfigInfoEncodedFormatterType1 # noqa: PLC0415
        from ..models.config_info_encoded_lsp_type_1 import ConfigInfoEncodedLspType1 # noqa: PLC0415
        from ..models.config_info_encoded_mcp import ConfigInfoEncodedMcp # noqa: PLC0415
        from ..models.config_info_encoded_media import ConfigInfoEncodedMedia # noqa: PLC0415
        from ..models.config_info_encoded_model_type_1 import ConfigInfoEncodedModelType1 # noqa: PLC0415
        from ..models.config_info_encoded_policies_item import ConfigInfoEncodedPoliciesItem # noqa: PLC0415
        from ..models.config_info_encoded_providers import ConfigInfoEncodedProviders # noqa: PLC0415
        from ..models.config_info_encoded_references import ConfigInfoEncodedReferences # noqa: PLC0415
        from ..models.config_info_encoded_tool_output import ConfigInfoEncodedToolOutput # noqa: PLC0415
        from ..models.config_info_encoded_watcher import ConfigInfoEncodedWatcher # noqa: PLC0415
        from ..models.config_plugin_entry_encoded import ConfigPluginEntryEncoded # noqa: PLC0415
        from ..models.config_warming_encoded import ConfigWarmingEncoded # noqa: PLC0415
        from ..models.config_web_search_info_encoded import ConfigWebSearchInfoEncoded # noqa: PLC0415
        from ..models.config_worktree import ConfigWorktree # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        schema = self.schema

        agents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = self.agents.to_dict()

        commands: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = self.commands.to_dict()

        compaction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compaction, Unset):
            compaction = self.compaction.to_dict()

        default_agent = self.default_agent

        enterprise: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enterprise, Unset):
            enterprise = self.enterprise.to_dict()

        experimental: dict[str, Any] | Unset = UNSET
        if not isinstance(self.experimental, Unset):
            experimental = self.experimental.to_dict()

        formatter: bool | dict[str, Any] | Unset
        if isinstance(self.formatter, Unset):
            formatter = UNSET
        elif isinstance(self.formatter, ConfigInfoEncodedFormatterType1):
            formatter = self.formatter.to_dict()
        else:
            formatter = self.formatter

        instructions: list[str] | Unset = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = self.instructions



        lsp: bool | dict[str, Any] | Unset
        if isinstance(self.lsp, Unset):
            lsp = UNSET
        elif isinstance(self.lsp, ConfigInfoEncodedLspType1):
            lsp = self.lsp.to_dict()
        else:
            lsp = self.lsp

        mcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcp, Unset):
            mcp = self.mcp.to_dict()

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        model: dict[str, Any] | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ConfigInfoEncodedModelType1):
            model = self.model.to_dict()
        else:
            model = self.model

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for componentsschemas_permission_ruleset_item_data in self.permissions:
                componentsschemas_permission_ruleset_item = componentsschemas_permission_ruleset_item_data.to_dict()
                permissions.append(componentsschemas_permission_ruleset_item)



        plugins: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = []
            for plugins_item_data in self.plugins:
                plugins_item: dict[str, Any] | str
                if isinstance(plugins_item_data, ConfigPluginEntryEncoded):
                    plugins_item = plugins_item_data.to_dict()
                else:
                    plugins_item = plugins_item_data
                plugins.append(plugins_item)



        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)



        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        references: dict[str, Any] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        share: str | Unset = UNSET
        if not isinstance(self.share, Unset):
            share = self.share.value


        shell = self.shell

        skills: list[str] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = self.skills



        snapshots = self.snapshots

        tool_output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_output, Unset):
            tool_output = self.tool_output.to_dict()

        update: str | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.value


        username = self.username

        warming: bool | dict[str, Any] | Unset
        if isinstance(self.warming, Unset):
            warming = UNSET
        elif isinstance(self.warming, ConfigWarmingEncoded):
            warming = self.warming.to_dict()
        else:
            warming = self.warming

        watcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watcher, Unset):
            watcher = self.watcher.to_dict()

        websearch: bool | dict[str, Any] | Unset
        if isinstance(self.websearch, Unset):
            websearch = UNSET
        elif isinstance(self.websearch, ConfigWebSearchInfoEncoded):
            websearch = self.websearch.to_dict()
        else:
            websearch = self.websearch

        worktree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worktree, Unset):
            worktree = self.worktree.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if agents is not UNSET:
            field_dict["agents"] = agents
        if commands is not UNSET:
            field_dict["commands"] = commands
        if compaction is not UNSET:
            field_dict["compaction"] = compaction
        if default_agent is not UNSET:
            field_dict["default_agent"] = default_agent
        if enterprise is not UNSET:
            field_dict["enterprise"] = enterprise
        if experimental is not UNSET:
            field_dict["experimental"] = experimental
        if formatter is not UNSET:
            field_dict["formatter"] = formatter
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if lsp is not UNSET:
            field_dict["lsp"] = lsp
        if mcp is not UNSET:
            field_dict["mcp"] = mcp
        if media is not UNSET:
            field_dict["media"] = media
        if model is not UNSET:
            field_dict["model"] = model
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if policies is not UNSET:
            field_dict["policies"] = policies
        if providers is not UNSET:
            field_dict["providers"] = providers
        if references is not UNSET:
            field_dict["references"] = references
        if share is not UNSET:
            field_dict["share"] = share
        if shell is not UNSET:
            field_dict["shell"] = shell
        if skills is not UNSET:
            field_dict["skills"] = skills
        if snapshots is not UNSET:
            field_dict["snapshots"] = snapshots
        if tool_output is not UNSET:
            field_dict["tool_output"] = tool_output
        if update is not UNSET:
            field_dict["update"] = update
        if username is not UNSET:
            field_dict["username"] = username
        if warming is not UNSET:
            field_dict["warming"] = warming
        if watcher is not UNSET:
            field_dict["watcher"] = watcher
        if websearch is not UNSET:
            field_dict["websearch"] = websearch
        if worktree is not UNSET:
            field_dict["worktree"] = worktree

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded_agents import ConfigInfoEncodedAgents # noqa: PLC0415
        from ..models.config_info_encoded_commands import ConfigInfoEncodedCommands # noqa: PLC0415
        from ..models.config_info_encoded_compaction import ConfigInfoEncodedCompaction # noqa: PLC0415
        from ..models.config_info_encoded_enterprise import ConfigInfoEncodedEnterprise # noqa: PLC0415
        from ..models.config_info_encoded_experimental import ConfigInfoEncodedExperimental # noqa: PLC0415
        from ..models.config_info_encoded_formatter_type_1 import ConfigInfoEncodedFormatterType1 # noqa: PLC0415
        from ..models.config_info_encoded_lsp_type_1 import ConfigInfoEncodedLspType1 # noqa: PLC0415
        from ..models.config_info_encoded_mcp import ConfigInfoEncodedMcp # noqa: PLC0415
        from ..models.config_info_encoded_media import ConfigInfoEncodedMedia # noqa: PLC0415
        from ..models.config_info_encoded_model_type_1 import ConfigInfoEncodedModelType1 # noqa: PLC0415
        from ..models.config_info_encoded_policies_item import ConfigInfoEncodedPoliciesItem # noqa: PLC0415
        from ..models.config_info_encoded_providers import ConfigInfoEncodedProviders # noqa: PLC0415
        from ..models.config_info_encoded_references import ConfigInfoEncodedReferences # noqa: PLC0415
        from ..models.config_info_encoded_tool_output import ConfigInfoEncodedToolOutput # noqa: PLC0415
        from ..models.config_info_encoded_watcher import ConfigInfoEncodedWatcher # noqa: PLC0415
        from ..models.config_plugin_entry_encoded import ConfigPluginEntryEncoded # noqa: PLC0415
        from ..models.config_warming_encoded import ConfigWarmingEncoded # noqa: PLC0415
        from ..models.config_web_search_info_encoded import ConfigWebSearchInfoEncoded # noqa: PLC0415
        from ..models.config_worktree import ConfigWorktree # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        _agents = d.pop("agents", UNSET)
        agents: ConfigInfoEncodedAgents | Unset
        if isinstance(_agents,  Unset):
            agents = UNSET
        else:
            agents = ConfigInfoEncodedAgents.from_dict(_agents)




        _commands = d.pop("commands", UNSET)
        commands: ConfigInfoEncodedCommands | Unset
        if isinstance(_commands,  Unset):
            commands = UNSET
        else:
            commands = ConfigInfoEncodedCommands.from_dict(_commands)




        _compaction = d.pop("compaction", UNSET)
        compaction: ConfigInfoEncodedCompaction | Unset
        if isinstance(_compaction,  Unset):
            compaction = UNSET
        else:
            compaction = ConfigInfoEncodedCompaction.from_dict(_compaction)




        default_agent = d.pop("default_agent", UNSET)

        _enterprise = d.pop("enterprise", UNSET)
        enterprise: ConfigInfoEncodedEnterprise | Unset
        if isinstance(_enterprise,  Unset):
            enterprise = UNSET
        else:
            enterprise = ConfigInfoEncodedEnterprise.from_dict(_enterprise)




        _experimental = d.pop("experimental", UNSET)
        experimental: ConfigInfoEncodedExperimental | Unset
        if isinstance(_experimental,  Unset):
            experimental = UNSET
        else:
            experimental = ConfigInfoEncodedExperimental.from_dict(_experimental)




        def _parse_formatter(data: object) -> bool | ConfigInfoEncodedFormatterType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                formatter_type_1 = ConfigInfoEncodedFormatterType1.from_dict(data)



                return formatter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | ConfigInfoEncodedFormatterType1 | Unset, data)

        formatter = _parse_formatter(d.pop("formatter", UNSET))


        instructions = cast(list[str], d.pop("instructions", UNSET))


        def _parse_lsp(data: object) -> bool | ConfigInfoEncodedLspType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lsp_type_1 = ConfigInfoEncodedLspType1.from_dict(data)



                return lsp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | ConfigInfoEncodedLspType1 | Unset, data)

        lsp = _parse_lsp(d.pop("lsp", UNSET))


        _mcp = d.pop("mcp", UNSET)
        mcp: ConfigInfoEncodedMcp | Unset
        if isinstance(_mcp,  Unset):
            mcp = UNSET
        else:
            mcp = ConfigInfoEncodedMcp.from_dict(_mcp)




        _media = d.pop("media", UNSET)
        media: ConfigInfoEncodedMedia | Unset
        if isinstance(_media,  Unset):
            media = UNSET
        else:
            media = ConfigInfoEncodedMedia.from_dict(_media)




        def _parse_model(data: object) -> ConfigInfoEncodedModelType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_1 = ConfigInfoEncodedModelType1.from_dict(data)



                return model_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigInfoEncodedModelType1 | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionRule] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for componentsschemas_permission_ruleset_item_data in _permissions:
                componentsschemas_permission_ruleset_item = PermissionRule.from_dict(componentsschemas_permission_ruleset_item_data)



                permissions.append(componentsschemas_permission_ruleset_item)


        _plugins = d.pop("plugins", UNSET)
        plugins: list[ConfigPluginEntryEncoded | str] | Unset = UNSET
        if _plugins is not UNSET:
            plugins = []
            for plugins_item_data in _plugins:
                def _parse_plugins_item(data: object) -> ConfigPluginEntryEncoded | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        plugins_item_type_1 = ConfigPluginEntryEncoded.from_dict(data)



                        return plugins_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(ConfigPluginEntryEncoded | str, data)

                plugins_item = _parse_plugins_item(plugins_item_data)

                plugins.append(plugins_item)


        _policies = d.pop("policies", UNSET)
        policies: list[ConfigInfoEncodedPoliciesItem] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ConfigInfoEncodedPoliciesItem.from_dict(policies_item_data)



                policies.append(policies_item)


        _providers = d.pop("providers", UNSET)
        providers: ConfigInfoEncodedProviders | Unset
        if isinstance(_providers,  Unset):
            providers = UNSET
        else:
            providers = ConfigInfoEncodedProviders.from_dict(_providers)




        _references = d.pop("references", UNSET)
        references: ConfigInfoEncodedReferences | Unset
        if isinstance(_references,  Unset):
            references = UNSET
        else:
            references = ConfigInfoEncodedReferences.from_dict(_references)




        _share = d.pop("share", UNSET)
        share: ConfigInfoEncodedShare | Unset
        if isinstance(_share,  Unset):
            share = UNSET
        else:
            share = ConfigInfoEncodedShare(_share)




        shell = d.pop("shell", UNSET)

        skills = cast(list[str], d.pop("skills", UNSET))


        snapshots = d.pop("snapshots", UNSET)

        _tool_output = d.pop("tool_output", UNSET)
        tool_output: ConfigInfoEncodedToolOutput | Unset
        if isinstance(_tool_output,  Unset):
            tool_output = UNSET
        else:
            tool_output = ConfigInfoEncodedToolOutput.from_dict(_tool_output)




        _update = d.pop("update", UNSET)
        update: ConfigInfoEncodedUpdate | Unset
        if isinstance(_update,  Unset):
            update = UNSET
        else:
            update = ConfigInfoEncodedUpdate(_update)




        username = d.pop("username", UNSET)

        def _parse_warming(data: object) -> bool | ConfigWarmingEncoded | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                warming_type_1 = ConfigWarmingEncoded.from_dict(data)



                return warming_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | ConfigWarmingEncoded | Unset, data)

        warming = _parse_warming(d.pop("warming", UNSET))


        _watcher = d.pop("watcher", UNSET)
        watcher: ConfigInfoEncodedWatcher | Unset
        if isinstance(_watcher,  Unset):
            watcher = UNSET
        else:
            watcher = ConfigInfoEncodedWatcher.from_dict(_watcher)




        def _parse_websearch(data: object) -> bool | ConfigWebSearchInfoEncoded | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                websearch_type_1 = ConfigWebSearchInfoEncoded.from_dict(data)



                return websearch_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | ConfigWebSearchInfoEncoded | Unset, data)

        websearch = _parse_websearch(d.pop("websearch", UNSET))


        _worktree = d.pop("worktree", UNSET)
        worktree: ConfigWorktree | Unset
        if isinstance(_worktree,  Unset):
            worktree = UNSET
        else:
            worktree = ConfigWorktree.from_dict(_worktree)




        config_info_encoded = cls(
            schema=schema,
            agents=agents,
            commands=commands,
            compaction=compaction,
            default_agent=default_agent,
            enterprise=enterprise,
            experimental=experimental,
            formatter=formatter,
            instructions=instructions,
            lsp=lsp,
            mcp=mcp,
            media=media,
            model=model,
            permissions=permissions,
            plugins=plugins,
            policies=policies,
            providers=providers,
            references=references,
            share=share,
            shell=shell,
            skills=skills,
            snapshots=snapshots,
            tool_output=tool_output,
            update=update,
            username=username,
            warming=warming,
            watcher=watcher,
            websearch=websearch,
            worktree=worktree,
        )

        return config_info_encoded

